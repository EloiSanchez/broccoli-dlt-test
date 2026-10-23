# Broccoli DLT

Three DLT data sources are provided:

- **CRIS** – defined in `ingestion/sources/cris.py`
- **OpenAlex** – defined in `ingestion/sources/openalex.py`
- **OpenAIRE** – defined in `ingestion/sources/openaire.py`

## Setup & run

1. Place your secret configuration in `.dlt/secrets.toml`, taken from `.dlt/template_secrets.toml`
2. Prepare virtual environment

```bash
# Install dependencies with uv (reads pyproject.toml)
uv sync

```

3. Edit `main.py` to uncomment the desired `ingest_*` call before running.
4. Execute the ingestion script (Can take a while, especially for the CRIS repositories. Around 10-15 mins). Data should be ingested as declared in `.dlt/secrets.toml`:

```bash
uv run python main.py
```

5. If ingested data is not stored in `./data/`, modify sqlmesh's `config.yaml`.
6. Execute sqlmesh in a new environment (for instance `<your_name>_env`)

```bash
uv run sqlmesh plan <your_name>_dev
```

This will materialize all the models found in `models/`.

## Data

### Staging

For now, `staging` parses the raw data of a few of the CRIS repositories. It uses [blueprint models](https://sqlmesh.readthedocs.io/en/stable/concepts/models/sql_models/#sql-model-blueprinting) to create blueprints that create multiple models (one for CRIS repository) applying the same parsing and transformations.

### Silver

Here, we union all the CRIS repositories (currently loosing track of which row comes from which repository, but this could be changed) to create a common set of Data Models for publications, persons... The silver models take advantage of [user-defined macros](https://sqlmesh.readthedocs.io/en/stable/concepts/macros/sqlmesh_macros/#user-defined-macro-functions) and [variables](https://sqlmesh.readthedocs.io/en/stable/concepts/macros/sqlmesh_macros/#local-variables) to dynamically create the query for the unions.

If the data from the repositories varies wildly, we may run into issues during this step. We have to find the best way to normalize the data during ingestion/parsing. An example of added complexity is L42 in `models/staging/cris/stg_cris__persons.sql#L42`. The row with `aid='openaire_cris_persons/37e19dcf-a864-49a4-980b-8e173237d98f'` coming from the `persons` set form `hva` returns a variant/json (`'{...}'`) instead of a list of variant/json (`[{...}]`), which makes the query fail if the explicit `coalesce` with `try_cast` is not added to handle the special case.

### Gold

As an example, we materialize a table containing a query that finds the publications of each author. Of course, data is quite minimal in this example and there is no assurance that authors found through `publications` are found in the data found fro `persons` (used to enrich the results).

## Dev features

### DAG

An HTML file of the dag can be created by executing:

```bash
uv run sqlmesh dag FILENAME [--select-model <MODEL_SELECTION>]
```

for instance, to see a dag of the gold model and its dependencies:

```bash
uv run sqlmesh dag gold_dag.html --select-model +gold.gold__author_publication_count
```

which will generate a file `gold_dag.html` that can be opened in the browser.

Moreover, the [vscode/vscodium extension](https://sqlmesh.readthedocs.io/en/stable/guides/vscode/) and the (deprecated) [local web ui](https://sqlmesh.readthedocs.io/en/stable/guides/ui/) offer ways to explore the lineage in an interactive way.

### LSP and formatting

There is an OSS LSP provided by sqlmesh that provides linting, diagnostics and formatting support in a strongly opinionated way. These tools are included by default in the VSCode extension, but can also be integrated with other editors with minor effort.
