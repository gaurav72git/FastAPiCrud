-- QUERY TO CREATE A TABLE

CREATE TABLE source_details (
    source_id SERIAL PRIMARY KEY,
    source VARCHAR(200) NOT NULL,
    source_type VARCHAR(10) NOT NULL,
    source_tag INTEGER,
    last_update_date timestamp without time zone NOT NULL DEFAULT now(),
    from_date timestamp without time zone NOT NULL DEFAULT now(),
    to_date timestamp without time zone NOT NULL DEFAULT now(),
    frequency VARCHAR(20)
);
