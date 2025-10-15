from extract import fetch_ecb_csv
from transform import melt_ecb
from load import upsert_fx_rates

if __name__ == "__main__":
    df_raw = fetch_ecb_csv()
    df_tidy = melt_ecb(df_raw)
    upsert_fx_rates(df_tidy)
    print("ETL done")
