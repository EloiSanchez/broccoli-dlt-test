MODEL (
  name silver.slv__cris_publications,
  kind VIEW
);

@DEF(cris_staging_tables, [
  'staging.stg_amsterdamumc__publications',
  'staging.stg_uva__publications',
  'staging.stg_hva__publications',
  'staging.stg_maastrichtuniversity__publications'
]);

WITH unioned AS (
  @union_multiple(@cris_staging_tables)
)
SELECT
  _dlt_load_id,
  _dlt_id,
  publication_aid,
  publication_id,
  axmlns,
  publication_category,
  language,
  title,
  subtitle,
  publication_year,
  scp_number,
  url,
  authors,
  publishers,
  status_scheme,
  status_text,
  access,
  isbn_medium,
  isbn_text
FROM unioned
