
> Neo4j default password is set to `neo-admin`

> You can set it to your preference when setting up the `dot-secrets`. It must look like `neo4j/<YOUR_PASSWORD>`


## Commands to remember

- To create the docker container: `sudo docker compose up -d` in quite mode.
- To create the docker container: `sudo docker compose up` more verbose.
- To open the Cypher terminal: `sudo docker exec --interactive --tty neo4j_server cypher-shell -u neo4j`


## Notes

- The APOC plugin is required to run the Graph Data Science plugin.

- APOC stands for **Awesome Procedures On Cypher.**

- Enabling `NEO4J_dbms_security_procedures_unrestricted=apoc.*` is generally acceptable in development environment, but in production you need to limit these privileges to only the procedures you trust (by whitelisting a minimal set). Not enabling this, would constantly run into errors due to access permissions. "The three backslashes `apoc.\\\*` are necessary to prevent wildcard expansions" was mentioned on the doc website, but my experiment proved otherwise.

- The `docker-compose.override.yml` is a way to modify the original `docker-compose.yml` at runtime. Used when some configurations need to be different based on the system running the container. For example when setting the memory limit between a laptop, desktop, or a production server.

- The folder structure under `volume` must exist before starting Docker, otherwise, Neo4j fails to start due to permissions errors.


## What value to set Neo4j's server memory `heap_initial__size` and `heap_max__size` variables?

Neo4j uses separate memory pools for the **JVM heap** (which holds objects, query processing data, etc.) and the **page cache** (which holds on-disk data in memory for fast access). The heap size settings you’re adjusting (initial and max) are for the JVM heap, not the page cache. For optimal performance, you often need to set both appropriately.

1. Set the heap size (initial and max) to the same value.
2. Start with 25–50% of the system's total memory (RAM).
3. Monitor and adjust using tools like VisualVM or GC logs.


## Using Docker Secrets?

Docker Secrets are secure and follows Docker's best practices, but requires **Docker Swarm** mode to be enabled, otherwise secrets won’t be mounted.

Note that Secrets only support environment variables starting with `NEO4J_` and ending with `_FILE`.

1. Create a new file `.secrets/neo4j_auth` that contains only the password line.
2. `docker-compose.yml` will look like this:

```yml
services:
  neo4j:
    ...
    environment:
      - NEO4J_AUTH_FILE=/run/secrets/neo4j_auth_file
      - ...
    secrets:
      - neo4j_auth_file

secrets:
  neo4j_auth_file:
    file: ./../.secrets/neo4j_auth
```


## Resources

- This [blog](https://medium.com/@matthewghannoum/simple-graph-database-setup-with-neo4j-and-docker-compose-061253593b5a)
- This [repository](https://github.com/Coding-Crashkurse/GraphRAG-with-Llama-3.1/blob/main/neo4j/Dockerfile)
- [Official Docs](https://neo4j.com/docs/operations-manual/current/docker/docker-compose-standalone/)

