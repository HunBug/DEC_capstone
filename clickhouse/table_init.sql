-- Case SENSITIVE column names! Confluent/Kafka creates all columns in upper case.

CREATE TABLE wiki_create_trans (
    DATABASE String,
    PAGE_ID UInt32,
    PAGE_TITLE String,
    COMMENT String,
    DOMAIN String,
    ID String,
    DATETIME DateTime64
) ENGINE = MergeTree ORDER BY (DATABASE, DOMAIN, DATETIME)


CREATE TABLE wiki_create_ner (
    ID String,
    COMMENT String,
    IS_CARDINAL Boolean,
    IS_PERSON Boolean,
    IS_DATE Boolean,
    IS_WORK_OF_ART Boolean,
    IS_ORG Boolean
) ENGINE = MergeTree PRIMARY KEY (ID)

DROP VIEW IF EXISTS wiki_obt;
CREATE VIEW wiki_obt AS 
SELECT 
    t.COMMENT,
    t.DOMAIN,
    t.DATETIME,
    t.PAGE_TITLE,
    n.IS_CARDINAL,
    n.IS_DATE,
    n.IS_ORG,
    n.IS_PERSON,
    n.IS_WORK_OF_ART
FROM wiki_create_trans as t
INNER JOIN wiki_create_ner as n on t.ID = n.ID;

