# Week 6 Final Data Analytics Project

## E-Commerce Revenue & Profitability Intelligence

## 1. Project Overview

This project was developed as part of the Week 6 Final Data Analytics Internship Assignment. It demonstrates an end-to-end data analytics workflow using a realistic synthetic e-commerce sales dataset.

The project covers data generation, data preparation and cleaning, exploratory data analysis (EDA), statistical analysis, data visualization, Power BI dashboard development, and business insight generation.

The main focus of the project is to understand revenue and profitability performance while identifying the impact of product returns on business profitability.

---

## 2. Problem Statement

E-commerce businesses generate large volumes of transactional data containing information about sales, customers, products, regions, sales channels, discounts, returns, revenue, and profit.

However, raw business data may contain missing values, duplicate records, invalid values, and inconsistent records. Without proper preparation and analysis, it becomes difficult to identify the factors affecting business performance.

The objective of this project is to transform raw e-commerce transaction data into meaningful analytical insights and an interactive business intelligence dashboard that can help identify revenue drivers, profitability patterns, high-performing areas, and return-related profit leakage.

---

## 3. Project Objectives

The major objectives of the project are:

- Select and prepare a suitable business dataset.
- Identify and handle missing values and duplicate records.
- Detect and remove invalid or inconsistent records.
- Perform exploratory data analysis using Python.
- Analyse revenue, profit, categories, regions, sales channels, and returns.
- Identify trends, patterns, correlations, and outliers.
- Create meaningful data visualizations.
- Develop an interactive Power BI dashboard.
- Generate data-driven business insights and recommendations.
- Maintain the complete project using Git and GitHub.

---

## 4. Dataset Description

The project uses a realistic synthetic e-commerce sales dataset generated using Python for educational and analytical purposes.

The dataset contains transactional information covering:

- Orders and order dates
- Customers and customer segments
- Regions and cities
- Product categories and products
- Sales channels
- Quantity and pricing
- Discounts
- Shipping costs and payment fees
- Cost of goods
- Returns
- Net revenue
- Profit and profit margin
- Payment methods and order status

### Dataset Size

- Raw dataset: 2,510 records
- Raw attributes: 26 columns
- Cleaned dataset: 2,477 records
- Records removed during cleaning: 33

The raw dataset intentionally contained realistic data-quality issues to demonstrate the complete data preparation workflow.

---

## 5. Data Preparation and Cleaning

The raw dataset was inspected for data types, missing values, duplicate records, invalid numerical values, and incorrect dates.

The following data-quality issues were identified and addressed:

- Missing customer segment values
- Missing city values
- Missing payment method values
- Missing discount values
- Invalid negative quantities
- Invalid negative unit prices
- Discount percentages outside the valid 0–100% range
- Future-dated records
- Duplicate records

The following cleaning operations were performed:

1. Converted the Order_Date column into the appropriate datetime format.
2. Removed duplicate records.
3. Removed records with invalid quantities.
4. Removed records with invalid unit prices.
5. Removed records with invalid discount percentages.
6. Removed future-dated orders.
7. Filled missing categorical values using appropriate mode-based imputation.
8. Filled missing discount percentages using the median.
9. Recalculated profit margin using valid net revenue values.
10. Performed final data-quality validation.

After cleaning, the dataset contained 2,477 valid records with no remaining duplicate records or missing values.

---

## 6. Exploratory Data Analysis

Exploratory Data Analysis was performed using Python, Pandas, NumPy, Matplotlib, and Seaborn.

The analysis included:

- Descriptive statistics
- Monthly revenue and profit analysis
- Product category analysis
- Regional performance analysis
- Sales channel analysis
- Return analysis
- Return-related profit leakage analysis
- Correlation analysis
- Outlier analysis
- Product-level profitability analysis

### Key EDA Findings

- Total net revenue was approximately ₹92.15 lakh.
- Total profit was approximately ₹26.16 lakh.
- The West region generated the highest net revenue and profit.
- Electronics was the leading product category by revenue and profit.
- Website was the strongest sales channel by revenue and profit.
- Overall return rate was 7.11%.
- Returned orders created a significant negative impact on profitability.
- Home & Kitchen had the highest return rate and the largest return-related profit loss.
- Marketplace had the lowest profit margin among the three sales channels.
- Stationery had the highest profit margin and lowest return rate among the product categories.

---

## 7. Data Visualization

Seven major analytical visualizations were created to communicate important business patterns:

1. Monthly Net Revenue Trend
2. Net Revenue by Product Category
3. Total Profit by Region
4. Total Profit by Sales Channel
5. Impact of Returns on Total Profit
6. Return Rate by Product Category
7. Profit Margin by Sales Channel

These visualizations were used to identify trends, comparisons, relationships, and profitability patterns within the dataset.

---

## 8. Power BI Dashboard

An interactive Power BI dashboard titled:

**E-Commerce Revenue & Profitability Intelligence Dashboard**

was developed using the cleaned dataset.

### Key Performance Indicators

The dashboard includes three primary KPIs:

- **Net Revenue:** ₹9,214,991.26
- **Total Profit:** ₹2,615,976.06
- **Return Rate:** 7.11%

### Dashboard Visualizations

The dashboard includes visual analysis of:

- Net Revenue by Year
- Net Revenue by Product Category
- Total Profit by Region
- Total Profit by Sales Channel
- Impact of Returns on Total Profit
- Return Rate by Product Category
- Profit Margin by Sales Channel

### Interactive Filters

The dashboard provides three interactive slicers:

- Region
- Sales Channel
- Category

These filters allow users to explore business performance across different segments.

---

## 9. Business Insights

The analysis generated the following major business insights:

### 1. West Region Performance

The West region generated approximately ₹31.58 lakh in net revenue and ₹8.92 lakh in profit, making it the strongest-performing region.

### 2. Electronics Performance

Electronics generated approximately ₹27.17 lakh in net revenue and ₹7.27 lakh in profit, making it the leading product category.

### 3. Return-Related Profit Leakage

Returned orders represented only 7.11% of total orders but generated approximately ₹3.07 lakh in negative profit impact.

### 4. Home & Kitchen Return Risk

Home & Kitchen recorded the highest return rate of 8.91% and approximately ₹1.08 lakh in return-related profit loss.

### 5. Website Channel Performance

The Website generated approximately ₹41.04 lakh in net revenue and ₹12.30 lakh in profit, with a profit margin of approximately 29.98%.

### 6. Marketplace Performance

Marketplace recorded the lowest profit margin at approximately 25.29% and the highest return rate among the sales channels at 7.72%.

### 7. Stationery Efficiency

Stationery generated a lower overall revenue volume but achieved the highest profit margin of approximately 38.09% and the lowest return rate of 4.25%.

---

## 10. Business Recommendations

Based on the analytical findings, the following recommendations are proposed:

### 1. Reduce Return-Related Profit Leakage

The business should investigate return reasons in Home & Kitchen and Electronics. Product quality, packaging, product descriptions, fulfilment, and delivery handling should be reviewed to reduce unnecessary returns and improve profitability.

### 2. Optimize Sales Channel Performance

The business should continue strengthening the Website channel because of its strong revenue and profitability performance. At the same time, Marketplace pricing, fees, product listings, customer experience, and return patterns should be investigated to improve its lower margin and higher return rate.

### 3. Investigate Regional Return Patterns

The North region has the highest return rate at 8.01%. The business should investigate the underlying causes and use the stronger-performing West region as a benchmark for identifying effective operational practices.

---

## 11. Tools and Technologies

The following tools and technologies were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI
- Git
- GitHub
- Visual Studio Code

---

## 12. Project Structure

```text
Week6_Final_Data_Analytics_Project/
│
├── data/
│   ├── raw/
│   │   ├── ecommerce_sales_raw.csv
│   │   └── data_dictionary.csv
│   └── cleaned/
│       └── ecommerce_sales_cleaned.csv
│
├── notebooks/
│   └── Final_Data_Analytics_Project.ipynb
│
├── src/
│   └── generate_dataset.py
│
├── visualizations/
│   ├── visualization_01_monthly_revenue.png
│   ├── visualization_02_revenue_by_category.png
│   ├── visualization_03_profit_by_region.png
│   ├── visualization_04_profit_by_sales_channel.png
│   ├── visualization_05_return_impact_on_profit.png
│   ├── visualization_06_return_rate_by_category.png
│   └── visualization_07_profit_margin_by_sales_channel.png
│
├── powerbi/
│   └── Final_Data_Analytics_Dashboard.pbix
│
├── report/
│   └── Final_Data_Analytics_Project_Report.pdf
│
├── presentation/
│   └── Final_Data_Analytics_Project_Presentation.pptx
│
├── .gitignore
└── README.md