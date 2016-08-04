CREATE KEYSPACE IF NOT EXISTS cvs_poc WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

CREATE TABLE IF NOT EXISTS cvs_poc.image (
    upload_id int,
    image blob,
    PRIMARY KEY (upload_id)
);