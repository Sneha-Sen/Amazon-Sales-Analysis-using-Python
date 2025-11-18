# Amazon-Sales-Analysis-using-Python

A data analysis project exploring Amazon product sales, customer behaviour, and state-wise demand patterns using Python.

# Project Objective

The goal of this project is to analyze Amazon sales data to identify:

Most sold product sizes

Popular product categories

State-wise customer demand

B2B vs Retail purchase trends

Order and courier status analysis

This project demonstrates real-world data cleaning, EDA, grouping, and visualization skills used in Data Analyst roles.

# Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

# Data Cleaning Steps

Removed unnecessary columns (New, PendingS)

Handled missing values (dropna())

Converted postal code → integer

Converted Date column → datetime

Standardized column names

Converted Category to string

These steps ensure consistency and make the dataset ready for analysis.

# Exploratory Data Analysis
1️⃣ Size-wise sales

Grouped data by product size to identify which size sells the most.

➡️ M-size products have the highest demand.

2️⃣ Category analysis

Checked which product category customers purchase most.

➡️ T-shirts dominate the category distribution.

3️⃣ B2B vs Retail purchase

Counted B2B flag values.

➡️ 99.3% of buyers are normal retail customers; only 0.7% are B2B.

4️⃣ State-wise demand

Identified top 10 states with the highest number of orders and plotted a countplot.

➡️ Maharashtra has the highest number of buyers.

5️⃣ Scatter analysis

Plotted Category vs Size for pattern observation.

# Key Insights

The platform sells mostly M-size products, indicating ideal inventory stocking for that size.

T-shirts are the most popular category, suggesting strong demand for fashion apparels.

Almost the entire customer base consists of retail buyers, not businesses.

Maharashtra is the largest customer base, useful for regional marketing decisions.

Dataset required cleaning—postal code correction, datetime conversion—which shows your data preprocessing skills.

# What This Project Demonstrates

Ability to clean messy real-world data

Understanding of pandas functions

Groupby and aggregation

Visual analysis through plots

Interpreting business insights

Presenting conclusions clearly

Perfect for DA / Power BI / Analyst interviews.
