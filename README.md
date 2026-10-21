# Broccoli DLT

Three DLT data sources are provided:

- **CRIS** – defined in `ingestion/sources/cris.py`
- **OpenAlex** – defined in `ingestion/sources/openalex.py`
- **OpenAIRE** – defined in `ingestion/sources/openaire.py`

## Setup & run

Place your secret configuration in `.dlt/secrets.toml`, taken from `.dlt/template_secrets.toml`

```bash
# Install dependencies with uv (reads pyproject.toml)
uv sync

# Execute the pipeline (choose source in `main.py`)
uv run python main.py
```

Edit `main.py` to uncomment the desired `ingest_*` call before running.

Data should be ingested as declared in `.dlt/secrets.toml`
