from typing import NamedTuple


class OpenAireSet(NamedTuple):
    short_name: str
    openaire_name: str
    xml_xpath: str
    extract_key: str


class Repository(NamedTuple):
    base_url: str
    short_name: str
