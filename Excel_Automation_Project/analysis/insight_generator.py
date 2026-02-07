def generate_business_insights(kpis, trends, demand_insights):
    insights = []

    # KPI summary
    insights.append(f"Total Sales: {kpis.get('total_sales', 'N/A')}\n")
    insights.append(f"Total Orders: {kpis.get('total_orders', 'N/A')}\n")
    insights.append(f"Average Order Value: {kpis.get('average_order_value', 'N/A')}\n\n")

    # Trend summary (without best year/month)
    insights.append("Monthly Sales Trend:\n")
    monthly_sales = trends.get("monthly_sales")
    if monthly_sales is not None:
        insights.append(monthly_sales.to_string())
        insights.append("\n\n")

    insights.append("Yearly Sales Trend:\n")
    yearly_sales = trends.get("yearly_sales")
    if yearly_sales is not None:
        insights.append(yearly_sales.to_string())
        insights.append("\n\n")

    # Demand insights
    high_demand, low_demand = demand_insights
    insights.append("Top 10 High Demand Products:\n")
    insights.append(high_demand.to_string(index=False))
    insights.append("\n\n")
    insights.append("Top 10 Low Demand Products:\n")
    insights.append(low_demand.to_string(index=False))
    insights.append("\n\n")

    return "\n".join(insights)
