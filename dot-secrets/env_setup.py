#!/usr/bin/env python3

import re
import glob
import shutil
import tempfile
import subprocess
from pathlib import Path


def setup_env_files():
    # Set base path and create directory if needed
    base_path = Path("../.secrets")
    base_path.mkdir(exist_ok=True)

    # Track processed files for second stage
    processed_files = []

    print("\n>>> Stage 1: Copying/merging files")
    # Process all dot-* files - First stage: Copy or merge
    for dotfile in glob.glob("dot-*"):
        # Create the new filename (.env instead of dot-env)
        newname = "." + dotfile[4:]  # Remove 'dot-' prefix
        if newname.endswith(".toml"):
            newname = newname[:-5]  # Remove .toml suffix

        target_file = base_path / newname
        processed_files.append(target_file)

        # Copy if target doesn't exist, otherwise merge missing keys
        if not target_file.exists():
            shutil.copy(dotfile, target_file)
            print(f"  Created new file: {target_file}")
        else:
            print(f"  Updating missing keys in: {target_file}")

            # Read existing keys from target file
            existing_keys = set()
            with open(target_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        match = re.match(r"^\s*([A-Za-z0-9_]+)\s*=", line)
                        if match:
                            existing_keys.add(match.group(1))

            # Add keys that don't exist in the target file
            with open(dotfile, "r") as source_file, open(target_file, "a") as target:
                for line in source_file:
                    line = line.rstrip()
                    if line and not line.startswith("#"):
                        match = re.match(r"^\s*([A-Za-z0-9_]+)\s*=", line)
                        if match and match.group(1) not in existing_keys:
                            target.write(line + "\n")
                            print(f"    Added missing key: {match.group(1)}")

    print("\n>>> Stage 2: Processing file references")
    # Second stage: Process ${file:...} references in all files
    for target_file in processed_files:
        print(f"  Resolving file references in: {target_file}")
        temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)

        with open(target_file, "r") as f:
            for line in f:
                # Find all ${file:...} patterns, possibly with shell commands
                matches = re.findall(r"\$\{file:([^}|]+)(?:\s*\|\s*([^}]+))?\}", line)

                if matches:
                    for match in matches:
                        file_path, shell_cmd = match[0].strip(), match[1].strip() if len(match) > 1 and match[1] else None
                        ref_file = base_path / file_path
                        print(f"    Found file reference: {file_path} -> ", end="")

                        if ref_file.exists():
                            # Read file content and remove trailing whitespace
                            with open(ref_file, "r") as rf:
                                file_content = rf.read().strip()

                            # Process content through shell command if present
                            if shell_cmd:
                                print("running shell command -> ", end="")
                                try:
                                    # Create process with the file content as input
                                    process = subprocess.run(
                                        ["bash", "-c", shell_cmd],
                                        input=file_content,
                                        text=True,
                                        capture_output=True,
                                        check=True,
                                    )
                                    file_content = process.stdout.strip()
                                    print("processed -> ", end="")
                                except subprocess.CalledProcessError as e:
                                    print(f"Error: Command failed with {e.returncode}")
                                    print(f"Error output: {e.stderr}")

                            # Replace ${file:...} with content
                            original_pattern = (
                                f"${{file:{file_path}}}" if not shell_cmd else f"${{file:{file_path} | {shell_cmd}}}"
                            )
                            line = line.replace(original_pattern, file_content)

                            print("Resolved")
                        else:
                            print(f"Warning: Referenced file not found: {ref_file}")

                temp_file.write(line)
        temp_file.close()

        # Replace original with processed file
        shutil.move(temp_file.name, target_file)

    print("\n>>> Environment setup complete! <<<")


if __name__ == "__main__":
    setup_env_files()
