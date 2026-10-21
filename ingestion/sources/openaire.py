from dlt.sources.helpers.rest_client.paginators import JSONResponseCursorPaginator
from dlt.sources.rest_api import rest_api_source

openaire_source = rest_api_source(
    {
        "client": {
            "base_url": "https://api.openaire.eu/graph/v2",
            "paginator": JSONResponseCursorPaginator(
                cursor_path="header.nextCursor",
                cursor_param="cursor",
            ),
        },
        "resource_defaults": {
            "endpoint": {
                "params": {
                    "cursor": "*",
                    "pageSize": 100,
                }
            }
        },
        "resources": [
            {
                "name": "research_products",
                "endpoint": {
                    "path": "researchProducts",
                    "data_selector": "results",
                    "params": {
                        "relCommunityId": "netherlands",
                        "type": "publication",
                        "fromPublicationDate": "2026-10-01",
                        "toPublicationDate": "2026-10-01",
                    },
                },
            },
        ],
    },
    max_table_nesting=0,
)
