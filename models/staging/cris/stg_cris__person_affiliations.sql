MODEL (
  name staging.stg_@{cris}__person_affiliations,
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

WITH stg_persons AS (
  SELECT
    person_id,
    affiliation
  FROM staging.stg_@{cris}__persons
), parsed_person_affiliations AS (
  SELECT
    person_id,
    UNNEST(affiliation) ->> '$.OrgUnit."@id"' AS org_unit_id
  FROM stg_persons
)
SELECT
  person_id::TEXT,
  org_unit_id::TEXT
FROM parsed_person_affiliations
