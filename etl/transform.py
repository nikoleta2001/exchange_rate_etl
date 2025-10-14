import pandas as pd

def melt_ecb(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms ECB data from wide to long format.
    Columns: rate_date | currency | rate
    """

    df = df.rename(columns={"Date": "rate_date"})
    melted = df.melt(id_vars=["rate_date"], var_name="currency", value_name="rate")
    melted = melted.dropna(subset=["rate"])
    melted["rate_date"] = pd.to_datetime(melted["rate_date"], errors="coerce").dt.date
    melted["rate"] = melted["rate"].astype(float)
    return melted
