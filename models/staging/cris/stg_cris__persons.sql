MODEL (
  name staging.stg_@{cris}__persons,
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

WITH raw_persons AS (
  SELECT
    _dlt_id,
    _dlt_load_id,
    aid,
    person_name,
    scopus_author_id,
    orcid,
    affiliation
  FROM sources.cris.@{cris}_persons
), parsed_persons AS (
  SELECT
    aid,
    STR_SPLIT(aid, '/')[2] AS person_id,
    TRIM((
      person_name ->> '$.FamilyNames'
    ), '"') AS person_family_names,
    TRIM((
      person_name ->> '$.FirstNames'
    ), '"') AS person_first_names,
    scopus_author_id,
    orcid,
    COALESCE(TRY_CAST(affiliation AS JSON[]), TRY_CAST([affiliation] AS JSON[])) AS affiliation
  FROM raw_persons
)
SELECT
  aid::TEXT AS person_aid,
  person_id::TEXT,
  person_family_names::TEXT,
  person_first_names::TEXT,
  scopus_author_id::TEXT,
  orcid::TEXT,
  affiliation::JSON[]
FROM parsed_persons
