# analysis/chart_dashboard.py

import pandas as pd


def create_chart_dashboard(monthly_sales, yearly_sales, top_products):
    output_path = "outputs/chart_dashboard.xlsx"

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        workbook = writer.book

        # Monthly sales
        monthly_sales.to_excel(writer, sheet_name="Monthly_Sales")
        worksheet = writer.sheets["Monthly_Sales"]
        chart = workbook.add_chart({"type": "line"})

        chart.add_series({
            "name": "Monthly Sales",
            "categories": "=Monthly_Sales!A2:A13",
            "values": "=Monthly_Sales!B2:B13",
        })

        worksheet.insert_chart("D2", chart)

        # Yearly sales
        yearly_sales.to_excel(writer, sheet_name="Yearly_Sales")
        worksheet = writer.sheets["Yearly_Sales"]
        chart = workbook.add_chart({"type": "line"})

        chart.add_series({
            "name": "Yearly Sales",
            "categories": "=Yearly_Sales!A2:A10",
            "values": "=Yearly_Sales!B2:B10",
        })

        worksheet.insert_chart("D2", chart)

        # Top products
        top_products.to_excel(writer, sheet_name="Top_Products")
        worksheet = writer.sheets["Top_Products"]
        chart = workbook.add_chart({"type": "column"})

        chart.add_series({
            "name": "Top Products",
            "categories": "=Top_Products!A2:A6",
            "values": "=Top_Products!B2:B6",
        })

        worksheet.insert_chart("D2", chart)

    print("📊 chart_dashboard.xlsx created successfully")
