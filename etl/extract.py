import os
import io
import requests
import pandas as pd

ECB_RATES_URL = os.getenv("ECB_RATES_URL")

def fetch_ecb_csv() -> pd.DataFrame:

    """
    Fetches ECB rates (CSV).
    First column is 'Date', the rest are currencies (EUR base)
    """

    resp = requests.get(ECB_RATES_URL, timeout=30)
    resp.raise_for_status()
    csv_bytes = io.BytesIO(resp.content)
    df = pd.read_csv(csv_bytes)
    return df