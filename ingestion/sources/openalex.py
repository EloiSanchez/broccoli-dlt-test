from datetime import date

import dlt
from dlt.sources.helpers.rest_client.paginators import JSONResponseCursorPaginator
from dlt.sources.rest_api import rest_api_source

openalex_source = rest_api_source(
    {
        "client": {
            "base_url": "https://api.openalex.org/",
            "auth": {
                "type": "bearer",
                "token": dlt.secrets["openalex_api_key"],
            },
            "paginator": JSONResponseCursorPaginator(
                cursor_path="meta.next_cursor",
                cursor_param="cursor",
            ),
        },
        "resource_defaults": {
            "endpoint": {
                "params": {
                    "cursor": "*",
                    "per_page": 100,
                }
            }
        },
        "resources": [
            {
                "name": "works",
                "endpoint": {
                    "path": "works",
                    "data_selector": "results",
                    "params": {
                        "filter": (
                            "institutions.country_code:NL,"
                            "from_publication_date:2026-10-01,"
                            # f"to_publication_date:2026-10-01"
                            f"to_publication_date:{date.today().strftime("%Y-%m-%d")}"
                        ),
                    },
                },
            },
        ],
    },
    max_table_nesting=0,
)
