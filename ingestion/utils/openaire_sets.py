from ingestion.utils.types import OpenAireSet

OPENAIRE_SETS = {
    "publications": OpenAireSet(
        short_name="publications",
        openaire_name="openaire_cris_publications",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Publication",
        extract_key="Publication",
    ),
    "persons": OpenAireSet(
        short_name="persons",
        openaire_name="openaire_cris_persons",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Person",
        extract_key="Person",
    ),
    "patents": OpenAireSet(
        short_name="patents",
        openaire_name="openaire_cris_patents",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Patent",
        extract_key="Patent",
    ),
    "orgunits": OpenAireSet(
        short_name="orgunits",
        openaire_name="openaire_cris_orgunits",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}OrgUnit",
        extract_key="OrgUnit",
    ),
    "events": OpenAireSet(
        short_name="events",
        openaire_name="openaire_cris_events",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Event",
        extract_key="Event",
    ),
    "equipments": OpenAireSet(
        short_name="equipments",
        openaire_name="openaire_cris_equipments",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Equipment",
        extract_key="Equipment",
    ),
    "products": OpenAireSet(
        short_name="products",
        openaire_name="openaire_cris_products",
        xml_xpath=".//{https://www.openaire.eu/cerif-profile/1.2/}Product",
        extract_key="Product",
    ),
}
