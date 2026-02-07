import pandas as pd

def demand_reason_analysis(df: pd.DataFrame):
    """
    Identifies high-demand and low-demand patterns with reasons.
    Returns two DataFrames:
    1) High demand reasons
    2) Low demand reasons
    """
    df: DataFrame  # hint for IDE
    if "orderdate" in df.columns:
        df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")
    if "month" not in df.columns:
        df["month"] = df["orderdate"].dt.month
    # Safety checks
    required_cols = ["sales", "month", "productline", "dealsize"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # -------- High Demand --------
    high_demand = (
        df.groupby(["month", "productline", "dealsize"])["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
        .head(10)
    )

    high_demand["reason"] = (
        "High sales driven by strong product demand and favorable deal size"
    )

    # -------- Low Demand --------
    low_demand = (
        df.groupby(["month", "productline", "dealsize"])["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=True)
        .head(10)
    )

    low_demand["reason"] = (
        "Low sales possibly due to weak demand, pricing, or off-season period"
    )

    return high_demand, low_demand


# test run
if __name__ == "__main__":
    from imp_csv import load_data
    from analysis.data_cleaning import clean_data

    raw = load_data()
    clean = clean_data(raw)

    # Ensure 'orderdate' is datetime
    if "orderdate" in clean.columns:
        clean["orderdate"] = pd.to_datetime(clean["orderdate"], errors="coerce")

    # Add month column if missing
    if "month" not in clean.columns:
        clean["month"] = clean["orderdate"].dt.month

    high, low = demand_reason_analysis(clean)
    print("HIGH DEMAND")
    print(high.head())
    print("\nLOW DEMAND")
    print(low.head())



