import dlt
from ingestion.sources.cris import CRIS_SOURCES
from ingestion.sources.openalex import openalex_source
from ingestion.sources.openaire import openaire_source


def ingest_cris():
    pipeline = dlt.pipeline(
        pipeline_name="cris",
        dataset_name="cris",
        destination=dlt.destinations.ducklake(),
    )
    pipeline.run([source for source in CRIS_SOURCES.values()])


def ingest_openalex():
    pipeline = dlt.pipeline(
        pipeline_name="openalex",
        dataset_name="openalex",
        destination=dlt.destinations.ducklake(),
    )

    pipeline.run(openalex_source)


def ingest_openaire():
    pipeline = dlt.pipeline(
        pipeline_name="opeanire",
        dataset_name="openaire",
        destination=dlt.destinations.ducklake(),
    )

    pipeline.run(openaire_source)


if __name__ == "__main__":
    ingest_cris()  # For now it makes max 3 requests per set and repository
    ingest_openalex()
    ingest_openaire()
