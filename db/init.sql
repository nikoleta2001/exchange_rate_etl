CREATE SCHEMA IF NOT EXISTS etl;

CREATE TABLE IF NOT EXISTS etl.fx_rates (
    rate_date   date        NOT NULL,
    currency    text        NOT NULL,
    rate        numeric     NOT NULL,
    ingested_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (rate_date, currency)
);
