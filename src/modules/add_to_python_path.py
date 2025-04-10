#!/usr/bin/env python3

import os
from pathlib import Path


def add_folder_to_pythonpath(folder_path=None):
    """
    Add a specified folder to PYTHONPATH by creating or updating project_dir.pth in the site-packages directory of the virtual environment.

    Usage:
    1. Run it as a script:
        ```bash
        python add_to_pythonpath.py /path/to/folder
        ```

    2. Import it in other Python code:
        ```python
        from add_to_pythonpath import add_folder_to_pythonpath

        # Add a specific folder
        add_folder_to_pythonpath('/path/to/folder')

        # Add current directory
        add_folder_to_pythonpath()
       ```

    Args:
        folder_path (str, optional): Path to the folder to add. If None, uses current working directory.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Use current directory if no folder specified
        if folder_path is None:
            folder_path = os.getcwd()
        
        # Convert to absolute path
        folder_path = os.path.abspath(folder_path)
        print(f"Adding folder to PYTHONPATH: {folder_path}")
        
        # Find the site-packages directory
        venv_path = Path('.venv/lib')
        if not venv_path.exists():
            print(f"Error: Virtual environment not found at {venv_path}")
            return False
            
        # Find Python version directory (python3.X)
        python_dirs = list(venv_path.glob('python*'))
        if not python_dirs:
            print("Error: Could not find Python directory in virtual environment")
            return False
            
        # Get site-packages path
        site_packages = python_dirs[0] / 'site-packages'
        if not site_packages.exists():
            print(f"Error: site-packages directory not found at {site_packages}")
            return False
            
        # Create or update project_dir.pth
        pth_file = site_packages / 'project_dir.pth'
        
        # Check if path already exists in the file
        if pth_file.exists():
            with open(pth_file, 'r') as f:
                paths = f.read().splitlines()
            if folder_path in paths:
                print(f"Path already exists in {pth_file}")
                return True
        
        # Append the folder path to the .pth file
        with open(pth_file, 'a+') as f:
            f.write(f"{folder_path}\n")
            
        print(f"Successfully added {folder_path} to {pth_file}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Use command line argument if provided, otherwise use current directory
    import argparse
    parser = argparse.ArgumentParser(description='Add a folder to PYTHONPATH')
    parser.add_argument('folder', nargs='?', default=None, 
                        help='Folder path to add (default: current directory)')
    args = parser.parse_args()
    
    add_folder_to_pythonpath(args.folder)