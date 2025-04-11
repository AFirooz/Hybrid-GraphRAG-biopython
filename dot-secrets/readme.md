# Introduction to `.secrets` and `.env`

This file will be used with dotenv package, see https://pypi.org/project/python-dotenv/ for more details.

> NOT ALL KEYS ARE REQUIRED!

- The `.env-docker-neo4j` is expected to be used by the docker composer to set the default password for neo4j's db password, while `.env` is expected to be used by the client (Jupyter notebooks) to interact with the db.


## Helping Script

The `dot-` in the file (or directory) names refers to substituting them with `.` in your cloned files. This is used to help you get started with environment variables.
Essentially you will have to copy the `dot-secrets` to `.secrets` and any `dot-env...` to `.env...`. To help with this, the `env_setup.py` script was created by AI and verified by me. It will:

1. Creates`.secrets` directory

2. For each dot-* file:
    - if the _target doesn't exist,_ copies the file with the correct naming.
    - if the _target exists,_ only adds keys that aren't already present.

3. Resolves any `${file:...}` references by replacing the pattern with the file content.
    
    **For example:**

    ```toml
    # import password from file and remove "neo4j/" prefix if present
    NEO4J_PASSWORD = "${file:.env-docker-neo4j | sed 's/.*\/\([^\"]*\)\".*/\1/'}"
    ```
    when the above variable is resolved, it will first look for `.env-docker-neo4j` file to get it's content (it should include only one line with `key = "value"` structure). The content will replace `file:.env-docker-neo4j`. Then the `env_setup.py` will process this command in the shell: `$("<content>" | sed 's/.*\/\([^\"]*\)\".*/\1/')`.
    
    The `sed ...` part is responsible for converting `NEO4J_PASSWORD = "neo4j/neo-admin"` to `"neo-admin"`.

## Setting Up APIs

- [LangSmith API](https://smith.langchain.com)
- [OpenAI API](https://platform.openai.com/api-keys)
- [Google Gemini API](https://ai.dev)
- [MongoDB Atlas](https://cloud.mongodb.com) -> Clusters -> Connect -> Driver -> Python

  For additional help with connection strings, [see here](https://www.mongodb.com/docs/atlas/troubleshoot-connection/#special-characters-in-connection-string-password).
- [Neo4j AuraDB](https://console.neo4j.io) and [here](# https://neo4j.com/docs/aura/classic/auradb/getting-started/create-database/) you can read how to create a database.
