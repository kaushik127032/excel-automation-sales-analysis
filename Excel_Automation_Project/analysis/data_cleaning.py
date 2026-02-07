import pandas as pd


def clean_data(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw sales data and return cleaned DataFrame
    """

    data = input_df.copy()

    # 1️⃣ Remove duplicate rows
    data = data.drop_duplicates()

    # 2️⃣ Standardize column names
    data.columns = (
        data.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 3️⃣ Convert order date to datetime
    if "orderdate" in data.columns:
        data["orderdate"] = pd.to_datetime(data["orderdate"], errors="coerce")

    # 4️⃣ Convert numeric columns safely
    numeric_cols = [
        "ordernumber",
        "quantityordered",
        "priceeach",
        "sales",
        "msrp"
    ]

    # Remove invalid quantity rows
    if "quantityordered" in data.columns:
        data = data[data["quantityordered"] > 0]

    for col in numeric_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    # 5️⃣ Drop rows where critical fields are missing
    critical_cols = ["ordernumber", "orderdate", "sales"]
    data = data.dropna(subset=[c for c in critical_cols if c in data.columns])

    return data


# test run
if __name__ == "__main__":
    from load_data import load_data

    raw_df = load_data()
    clean_df = clean_data(raw_df)

    print("Before cleaning:", raw_df.shape)
    print("After cleaning :", clean_df.shape)
    print(clean_df.head())
