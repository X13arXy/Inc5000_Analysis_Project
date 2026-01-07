# 📈 Inc. 5000 Analysis: Revenue Growth & Workforce Efficiency

## 📌 Project Overview
This end-to-end data analysis project explores the financial performance and workforce dynamics of the **Inc. 5000** list (fastest-growing private companies in the US).

The primary objective was to investigate the correlation between **revenue growth** and **headcount changes**, identifying industries that managed to scale revenue while optimizing or reducing their workforce.

## 🛠️ Tech Stack & Workflow
This project simulates a full Data Analyst workflow, moving from raw data to actionable business insights:

* **Python (Pandas):** * ETL process: Cleaning raw CSV data.
    * Data transformation: Converting currency strings to integers, handling missing values, and normalizing industry names.
* **SQL:** * Data Aggregation: Grouping companies by industry to calculate averages.
    * Business Logic: Writing queries to isolate companies with the "Growth Paradox" (positive revenue growth with negative hiring trends).
* **Power BI:** * Data Modeling: Establishing relationships between datasets.
    * DAX Measures: Creating custom calculations for dynamic analysis.
    * Data Storytelling: Designing an interactive dashboard to visualize the findings.

## 🔍 Key Insights & Findings
1.  **The Efficiency Paradox:** The *Business Products & Services* industry demonstrated a unique trend—significant revenue growth despite a notable reduction in headcount. This suggests a shift towards automation or high-value service models.
2.  **Top Revenue Generators:** The *Security* and *Health* sectors lead the market in terms of average revenue per company.
3.  **Growth Leaders:** While traditional industries have high revenue, the *Logistics & Transportation* sector showed the highest average percentage growth rate.

## 📊 Dashboard Preview

### Main Dashboard View
*(An overview of industry performance)*
![Dashboard Overview](images/dashboard_full.png)



## 📂 Repository Structure
```text
├── data/               # Raw and processed datasets (CSV)
├── python_scripts/     # Python ETL scripts (Jupyter Notebook or .py)
├── sql_queries/        # SQL scripts used for data aggregation
├── power_bi/           # Power BI Project file (.pbix)
├── images/             # Screenshots for README
└── README.md           # Project documentation