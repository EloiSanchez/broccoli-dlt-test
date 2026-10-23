MODEL (
  name staging.stg_@{cris}__publication_authors,
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

WITH raw_publication_authors AS (
  SELECT
    publication_id,
    UNNEST((
      authors ->> '$.Author[*].Person'
    )::JSON[]) AS author
  FROM staging.stg_@{cris}__publications
), flattened_publication_authors AS (
  SELECT
    publication_id,
    TRIM(author."@id", '"') AS author_id
  FROM raw_publication_authors
)
SELECT
  publication_id::TEXT,
  author_id::TEXT
FROM flattened_publication_authors
