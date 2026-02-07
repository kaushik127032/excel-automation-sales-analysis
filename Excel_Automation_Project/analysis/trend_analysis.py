import pandas as pd

def trend_analysis(df: pd.DataFrame) -> dict:
    """
    Analyze monthly and yearly sales trends
    """

    # Ensure datetime
    df["orderdate"] = pd.to_datetime(df["orderdate"])

    # Yearly trend
    yearly_sales = (
        df.groupby("year_id")["sales"]
        .sum()
        .sort_index()
        .reset_index()
    )

    # Monthly trend
    monthly_sales = (
        df.groupby("month_id")["sales"]
        .sum()
        .sort_index()
        .reset_index()
    )

    # Top products (by total sales)
    if "productline" in df.columns:
        top_products = (
            df.groupby("productline")["sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
    else:
        top_products = pd.DataFrame(columns=["productline", "sales"])

    # Best year (year with max sales)
    best_year = yearly_sales["sales"].idxmax() if not yearly_sales.empty else None

    return {
        "yearly_sales": yearly_sales,
        "monthly_sales": monthly_sales,
        "best_year": best_year,
        "top_products": top_products
    }
