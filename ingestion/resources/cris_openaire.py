from typing import Any, DefaultDict, Generator
from xml.etree import ElementTree as ET

import dlt
from dlt.extract.items import DataItemWithMeta
from dlt.sources.helpers import requests
import xmltodict

from ingestion.utils.types import OpenAireSet, Repository


@dlt.resource(write_disposition="replace")
def get_cris_set(
    repository: Repository, openaire_set: OpenAireSet, max_requests=5
) -> Generator[DataItemWithMeta, None, None]:
    target_table = f"{repository.short_name}_{openaire_set.short_name}"
    params = {
        "verb": "ListRecords",
        "metadataPrefix": "oai_cerif_openaire",
        "set": openaire_set.openaire_name,
    }

    request_number = 0
    while request_number < max_requests and params is not None:
        request_number += 1
        print(
            f"Requesting {request_number} from "
            f"{repository.short_name}:{openaire_set.short_name}"
        )

        # Perform request
        try:
            response = requests.get(repository.base_url, params=params, timeout=5)
            response.raise_for_status()
        except Exception as e:
            print(
                f"Found error in {repository.short_name}:{openaire_set.short_name}\n{e}"
            )
            break

        # Parse and return as xml
        root = ET.fromstring(response.text)
        yield dlt.mark.with_table_name(
            root.findall(openaire_set.xml_xpath),
            target_table,
        )

        # Paginate if needed. Do not add metadataPrefix to params or request errors
        resumption_token = root.find(
            ".//{http://www.openarchives.org/OAI/2.0/}resumptionToken"
        )
        if resumption_token is None or resumption_token.text is None:
            break

        params = {"verb": "ListRecords", "resumptionToken": resumption_token.text}


@dlt.transformer
def parse_set_records(
    page: ET.Element, openaire_set: OpenAireSet
) -> Generator[dict[Any, Any], None, None]:
    yield from (
        xmltodict.parse(
            ET.tostring(publication).decode(),
            process_namespaces=True,
            namespaces=DefaultDict(lambda: None),
        )[openaire_set.extract_key]
        for publication in page
    )
