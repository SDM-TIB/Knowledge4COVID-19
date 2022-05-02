# Pipeline Creations

This directory contains the instructions for running the K4COVID pipeline

- `scripts` - contains scripts used for transforming sources to RDF and loading it to triple store (Virtuoso)
      - `virtuoso-script.sh`  - used to remotely connect and load data using `isql-v` tool of virtuoso on command line
      - `load_to_virtuos.py` - used to load the transformed RDF data to virtuoso using the `virtuoso-script.sh` script
- `docker-compose.yml` - docker compose setup for transforming data to RDF and load it to `Virtuoso` triple store.

# Running the docker containers
To start the docker containers, run the following command
(Prerequisite: *Docker-ce*, *Docker-compose*)
```bash
docker-compose up -d
```
This command will download and start the three docker containers used in our pipeline
1) SDM-RDFizer
2) SPARQL Endpoint
3) Dereferencing Interface (Pubby)

# Creating RDF Dump using SDM-RDFizer

## Run `rdfizer` tool to create the RDF dump according to the above configuration and mapping files included in this config.

The docker container created above using the docker-compose.yaml file will attach this repository as volume at `/data` endpoint

```bash

docker exec -it sdmrdfizer /data/scripts/run_rdfizier.sh

```

This will create the RDF dumps according the configuration files in KGC-DIS directory, and store the RDF dump in `/rdf` directory, 
You can find the raw RDF file in `.nt` serialization inside 

- Load the RDF dump to Virtuoso


To load the generated RDF dump in step 2, we will use a script included in `scripts` folder as follows:

```bash

docker exec -it sdmrdfizer python3 /data/scripts/load_to_virtuoso.py

```

Before running this, make sure you update the environmental variable in the `docker-compose.yml` file.



4. Open [http://localhost:8891/sparql](http://localhost:8891/sparql) on your browser and you will get access to the created Knowledge Graph


