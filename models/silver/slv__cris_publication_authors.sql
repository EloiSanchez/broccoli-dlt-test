MODEL (
  name silver.slv__cris_publication_authors,
  kind VIEW
);

@DEF(cris_staging_tables, [
  'staging.stg_amsterdamumc__publication_authors',
  'staging.stg_uva__publication_authors',
  'staging.stg_hva__publication_authors',
  'staging.stg_maastrichtuniversity__publication_authors'
]);

WITH unioned AS (
  @union_multiple(@cris_staging_tables)
)
SELECT
  publication_id::TEXT,
  author_id::TEXT
FROM unioned
