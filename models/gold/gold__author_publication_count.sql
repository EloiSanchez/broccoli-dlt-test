/* Number of publications per author. 
If author not found in persons table, it is filtered out */
MODEL (
  name gold.gold__author_publication_count,
  kind FULL,
  grain author_id
);

WITH publication_authors /* Import CTE */ AS (
  SELECT
    author_id,
    publication_id
  FROM silver.slv__cris_publication_authors
), persons /* Import CTE */ AS (
  SELECT
    person_id,
    person_family_names,
    person_first_names,
    scopus_author_id,
    orcid
  FROM silver.slv__cris_persons
), author_publication_count_enriched /* 
Find number of publications per author and enrich. 
If no data to enrich, filter out. 
*/ AS (
  SELECT
    publication_authors.author_id,
    persons.person_family_names,
    persons.person_first_names,
    persons.scopus_author_id,
    persons.orcid,
    COUNT(*) AS publication_count
  FROM publication_authors
  LEFT JOIN persons
    ON publication_authors.author_id = persons.person_id
  GROUP BY
    author_id,
    person_family_names,
    person_first_names,
    scopus_author_id,
    orcid
  HAVING
    NOT person_family_names IS NULL
)
SELECT
  author_id,
  person_family_names,
  person_first_names,
  scopus_author_id,
  orcid,
  publication_count
FROM author_publication_count_enriched
