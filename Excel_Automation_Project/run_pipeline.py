# run_pipeline.py
# ================= MAIN ENTRY POINT =================

import os
import pandas as pd

from imp_csv import load_data
from analysis.data_cleaning import clean_data
from analysis.kpi_analysis import kpi_analysis
from analysis.trend_analysis import trend_analysis
from analysis.demand_reason_analysis import demand_reason_analysis
from analysis.insight_generator import generate_business_insights

# ✅ Use only dashboard folder chart_dashboard
from dashboard.chart_dashboard import create_chart_dashboard


def main():
    print("🚀 Pipeline started...")

    # Ensure outputs folder exists
    os.makedirs("outputs/charts", exist_ok=True)

    # 1️⃣ Load data
    df_raw = load_data()
    print("✅ Data loaded")

    # 2️⃣ Clean data
    df_clean = clean_data(df_raw)
    print("✅ Data cleaned")

    # --- Ensure month_id and year_id columns exist ---
    if "orderdate" in df_clean.columns:
        df_clean["orderdate"] = pd.to_datetime(df_clean["orderdate"], errors="coerce")
        if "month_id" not in df_clean.columns:
            df_clean["month_id"] = df_clean["orderdate"].dt.month
        if "year_id" not in df_clean.columns:
            df_clean["year_id"] = df_clean["orderdate"].dt.year

    # 3️⃣ KPI Analysis
    kpis = kpi_analysis(df_clean)
    print("✅ KPI analysis done")

    # 4️⃣ Trend Analysis
    trends = trend_analysis(df_clean)
    print("✅ Trend analysis done")

    # 5️⃣ Demand / Low performance reasons
    demand_insights = demand_reason_analysis(df_clean)
    print("✅ Demand analysis done")

    # 6️⃣ Generate business insights (text)
    insights_text = generate_business_insights(
        kpis,
        trends,
        demand_insights
    )

    with open("outputs/insight_summary.txt", "w", encoding="utf-8") as f:
        f.write(insights_text)

    print("📝 Insight summary generated")

    # 7️⃣ Create Excel chart dashboard
    create_chart_dashboard(
        monthly_sales=trends.get("monthly_sales"),
        yearly_sales=trends.get("yearly_sales"),
        top_products=trends.get("top_products")
    )

    print("📊 Chart dashboard created")
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()
