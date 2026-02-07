import pandas as pd
from imp_csv import load_data
from analysis.data_cleaning import clean_data


def kpi_analysis(df: pd.DataFrame) -> dict:
    return {
        "total_sales": df["sales"].sum(),
        "total_orders": df["ordernumber"].nunique(),
        "total_customers": df["customername"].nunique(),
        "avg_order_value": df["sales"].sum() / df["ordernumber"].nunique()
    }


if __name__ == "__main__":
    raw_df = load_data()
    clean_df = clean_data(raw_df)
    print(kpi_analysis(clean_df))
