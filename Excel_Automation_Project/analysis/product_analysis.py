import pandas as pd


def top_products_analysis(
    df: pd.DataFrame,
    top_n: int = 10
) -> pd.DataFrame:
    """
    Returns top N products by total sales
    """

    # Safety check
    required_cols = ["productline", "sales"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    top_products = (
        df.groupby("productline")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
        .head(top_n)
    )

    return top_products


# test run
if __name__ == "__main__":
    from imp_csv import load_data
    from analysis.data_cleaning import clean_data

    raw = load_data()
    clean = clean_data(raw)

    result = top_products_analysis(clean)
    print(result)
