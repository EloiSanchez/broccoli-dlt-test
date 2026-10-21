import dlt

from ingestion.resources.cris_openaire import get_cris_set, parse_set_records
from ingestion.utils.openaire_sets import OPENAIRE_SETS
from ingestion.utils.types import Repository


def cris_source_factory(repository: Repository, max_requests=3):
    @dlt.source(name=repository.short_name, max_table_nesting=0, parallelized=True)
    def cris_source():
        for openaire_set in OPENAIRE_SETS.values():
            resource = get_cris_set(
                repository, openaire_set, max_requests=max_requests
            ) | parse_set_records(openaire_set)
            yield resource.with_name(
                f"{repository.short_name}_{openaire_set.short_name}"
            )

    return cris_source()


CRIS_SOURCES = {
    "maastrichtuniversity": cris_source_factory(
        Repository(
            short_name="maastrichtuniversity",
            base_url="https://cris.maastrichtuniversity.nl/ws/oai",
        )
    ),
    "uci": cris_source_factory(
        Repository(
            short_name="uci",
            base_url="https://oamemtfp.uci.ru.nl/metis-oaipmh-endpoint/OAIHandler",
        )
    ),
    "amsterdamumc": cris_source_factory(
        Repository(
            short_name="amsterdamumc",
            base_url="https://pure.amsterdamumc.nl/ws/oai",
        )
    ),
    "eur": cris_source_factory(
        Repository(
            short_name="eur",
            base_url="https://pure.eur.nl/ws/oai",
        )
    ),
    "hva": cris_source_factory(
        Repository(
            short_name="hva",
            base_url="https://pure.hva.nl/ws/oai",
        )
    ),
    "rug": cris_source_factory(
        Repository(
            short_name="rug",
            base_url="https://pure.rug.nl/ws/oai",
        )
    ),
    "tudelft": cris_source_factory(
        Repository(
            short_name="tudelft",
            base_url="https://pure.tudelft.nl/ws/oai",
        )
    ),
    "tue": cris_source_factory(
        Repository(
            short_name="tue",
            base_url="https://pure.tue.nl/ws/oai",
        )
    ),
    "uva": cris_source_factory(
        Repository(
            short_name="uva",
            base_url="https://pure.uva.nl/ws/oai",
        )
    ),
    "uvt": cris_source_factory(
        Repository(
            short_name="uvt",
            base_url="https://pure.uvt.nl/ws/oai",
        )
    ),
    "uu": cris_source_factory(
        Repository(
            short_name="uu",
            base_url="https://research-portal.uu.nl/ws/oai",
        )
    ),
    "ou": cris_source_factory(
        Repository(
            short_name="ou",
            base_url="https://research.ou.nl/ws/oai",
        )
    ),
    "vu": cris_source_factory(
        Repository(
            short_name="vu",
            base_url="https://research.vu.nl/ws/oai",
        )
    ),
    "vumc": cris_source_factory(
        Repository(
            short_name="vumc",
            base_url="https://research.vumc.nl/ws/oai",
        )
    ),
    "utwente": cris_source_factory(
        Repository(
            short_name="utwente",
            base_url="https://ris.utwente.nl/ws/oai",
        )
    ),
}
