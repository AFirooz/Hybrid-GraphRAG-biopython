#!/usr/bin/env python3

import re
import glob
import shutil
import tempfile
from pathlib import Path

def setup_env_files():
    # Set base path and create directory if needed
    base_path = Path("../.secrets")
    base_path.mkdir(exist_ok=True)
    
    # Process all dot-* files
    for dotfile in glob.glob("dot-*"):
        # Create the new filename (.env instead of dot-env)
        newname = "." + dotfile[4:]  # Remove 'dot-' prefix
        if newname.endswith(".toml"):
            newname = newname[:-5]  # Remove .toml suffix
            
        target_file = base_path / newname
        
        # Copy if target doesn't exist, otherwise merge missing keys
        if not target_file.exists():
            shutil.copy(dotfile, target_file)
            print(f"\n>>> Created new file: {target_file}")
        else:
            print(f"\n>>> Updating missing keys in: {target_file}")
            
            # Read existing keys from target file
            existing_keys = set()
            with open(target_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        match = re.match(r'^\s*([A-Za-z0-9_]+)\s*=', line)
                        if match:
                            existing_keys.add(match.group(1))
            
            # Add keys that don't exist in the target file
            with open(dotfile, 'r') as source_file, open(target_file, 'a') as target:
                for line in source_file:
                    line = line.rstrip()
                    if line and not line.startswith('#'):
                        match = re.match(r'^\s*([A-Za-z0-9_]+)\s*=', line)
                        if match and match.group(1) not in existing_keys:
                            target.write(line + '\n')
                            print(f"  Added missing key: {match.group(1)}")
        
        # Process ${file:...} references
        print(f"\n>>> Resolving file references in: {target_file}")
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        
        with open(target_file, 'r') as f:
            for line in f:
                # Find all ${file:...} patterns
                matches = re.findall(r'\$\{file:([^}]+)\}', line)
                
                if matches:
                    for match in matches:
                        ref_file = base_path / match.strip()
                        print(f"  Found file reference: {match} -> ", end="")
                        
                        if ref_file.exists():
                            # Read file content and remove trailing whitespace
                            with open(ref_file, 'r') as rf:
                                file_content = rf.read().strip()
                            
                            # Replace ${file:...} with content
                            line = line.replace(f"${{file:{match}}}", file_content)
                            
                            print("Resolved")
                        else:
                            print(f"Warning: Referenced file not found: {ref_file}")

                temp_file.write(line)
        temp_file.close()
        
        # Replace original with processed file
        shutil.move(temp_file.name, target_file)
    
    print("\n\nEnvironment setup complete!")

if __name__ == "__main__":
    setup_env_files()