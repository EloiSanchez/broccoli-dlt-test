MODEL (
  name staging.stg_@{cris}__publications,
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

SELECT
  _dlt_load_id::TEXT,
  _dlt_id::TEXT,
  aid::TEXT AS publication_aid,
  STR_SPLIT(aid, '/')[2]::TEXT AS publication_id,
  axmlns::JSON,
  (
    type ->> '$.@publicationCategory'
  )::TEXT AS publication_category,
  language::TEXT,
  TRIM(title."#text", '"')::TEXT AS title,
  TRIM(subtitle."#text", '"')::TEXT AS subtitle,
  publication_date::INT AS publication_year,
  scp_number::TEXT,
  url::TEXT,
  authors::JSON,
  publishers::JSON,
  TRIM(status."@scheme", '"')::TEXT AS status_scheme,
  TRIM(status."#text", '"')::TEXT AS status_text,
  access::TEXT,
  TRIM(isbn."@medium", '"')::TEXT AS isbn_medium,
  TRIM(isbn."#text", '"')::TEXT AS isbn_text
FROM sources.cris.@{cris}_publications
