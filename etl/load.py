import os, psycopg2, psycopg2.extras, pandas as pd

def get_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB", "etl_db"),
        user=os.getenv("POSTGRES_USER", "etl_user"),
        password=os.getenv("POSTGRES_PASSWORD", "etl_pass"),
    )

def upsert_fx_rates(df: pd.DataFrame, batch_size: int = 5000):
    sql = """
    INSERT INTO etl.fx_rates (rate_date, currency, rate)
    VALUES (%s, %s, %s)
    ON CONFLICT (rate_date, currency) DO UPDATE
      SET rate = EXCLUDED.rate,
          ingested_at = now();
    """
    rows = list(df[["rate_date","currency","rate"]].itertuples(index=False, name=None))
    with get_conn() as conn:
        with conn.cursor() as cur:
            psycopg2.extras.execute_batch(cur, sql, rows, page_size=batch_size)
