CREATE OR REPLACE STREAM WIKI_CREATE_STREAM(
  database STRING,
  page_id INT,
  page_title STRING,
  comment STRING
  )
WITH (KAFKA_TOPIC='wiki_create', VALUE_FORMAT='JSON');

CREATE OR REPLACE STREAM WIKI_DELETE_STREAM(
  database STRING,
  page_id INT,
  page_title STRING,
  rev_count INT,
  comment STRING
  )
WITH (KAFKA_TOPIC='wiki_delete', VALUE_FORMAT='JSON');

CREATE OR REPLACE STREAM WIKI_CREATE_STREAM(
  database STRING,
  page_id INT,
  page_title STRING,
  comment STRING,
  meta STRUCT<domain STRING,
              id STRING,
              dt STRING
  >
  )
WITH (KAFKA_TOPIC='wiki_create', VALUE_FORMAT='JSON');

select 
  database,
  page_id,
  page_title,
  comment,
  meta->domain as domain,
  meta->id as id,
  STRINGTOTIMESTAMP(meta->dt, 'yyyy-MM-dd''T''HH:mm:ss''Z''') as datetime
from WIKI_CREATE_STREAM 
EMIT CHANGES LIMIT 4;

CREATE STREAM wiki_create_trans WITH (kafka_topic = 'wiki_create_trans') AS
select 
  database,
  page_id,
  page_title,
  comment,
  meta->domain as domain,
  meta->id as id,
  STRINGTOTIMESTAMP(meta->dt, 'yyyy-MM-dd''T''HH:mm:ss''Z''') as datetime
from WIKI_CREATE_STREAM 
EMIT CHANGES;