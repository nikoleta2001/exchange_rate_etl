from extract import fetch_ecb_csv
from transform import melt_ecb
from load import upsert_fx_rates
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

if __name__ == "__main__":
    try:
        df_raw = fetch_ecb_csv()
        df_tidy = melt_ecb(df_raw)
        upsert_fx_rates(df_tidy)
        print("ETL done")
    except Exception as e:
        logging.exception("ETL failed: %s", e)
        raise