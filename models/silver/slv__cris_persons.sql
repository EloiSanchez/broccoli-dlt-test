MODEL (
  name silver.slv__cris_persons,
  kind VIEW
);

@DEF(cris_staging_tables, [
  'staging.stg_amsterdamumc__persons', 
  'staging.stg_uva__persons',
  'staging.stg_hva__persons',
  'staging.stg_maastrichtuniversity__persons',
  ]);

WITH unioned AS (
  @union_multiple(@cris_staging_tables)
)
SELECT
  person_aid,
  person_id::TEXT,
  person_family_names::TEXT,
  person_first_names::TEXT,
  scopus_author_id::TEXT,
  orcid::TEXT,
  affiliation::JSON[]
FROM unioned
