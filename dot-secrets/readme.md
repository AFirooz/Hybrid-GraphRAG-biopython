# Introduction to `.secrets` and `.env`


- The `dot-` in the file (or directory) names refers to substituting them with `.` in your cloned files. This is used to help you get started with environment variables.

- In your cloned dir, copy the `dot-secrets` to `.secrets` and any `dot-env...` to `.env...`.

- The `env_setup.sh` script will:
    1. Creates`.secrets` directory
    
    2. For each dot-* file, if the target doesn't exist, copies the file. Otherwise, if the target exists, only adds keys that aren't already present.
    
    3. Resolves any ${file:...} references by replacing the pattern with the file content
