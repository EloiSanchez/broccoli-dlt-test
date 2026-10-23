MODEL (
  name staging.stg_@{cris}__publication_publishers,
  kind VIEW,
  blueprints (
    (
      cris := amsterdamumc
    ),
    (
      cris := maastrichtuniversity
    ),
    (
      cris := hva
    ),
    (
      cris := uva
    )
  )
);

WITH raw_publication_publishers AS (
  SELECT
    publication_id,
    publishers
  FROM staging.stg_@{cris}__publications
), parsed_publication_publishers AS (
  SELECT
    publication_id,
    publishers ->> '$.Publisher.OrgUnit.Name."#text"' AS publisher_name
  FROM raw_publication_publishers
)
SELECT
  publication_id::TEXT,
  publisher_name::TEXT
FROM parsed_publication_publishers
