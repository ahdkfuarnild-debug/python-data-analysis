Python Data Analysis Project

[![Tests](https://github.com/ahdkfuarnild-debug/python-data-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/ahdkfuarnild-debug/python-data-analysis/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)

A practical Python project for analyzing sales data and generating business-focused insights.

What it does

Sample results

The analysis of the included synthetic sales dataset produced the following example results:

* 500 orders
* 2,255 units sold
* $71,221.79 total revenue
* $36,753.51 total profit
* 51.60% profit margin
* Top category: Electronics
* Top product: Headphones


* Loads and validates sales data from CSV files
* Cleans and processes the dataset
* Calculates revenue, cost, profit, and key performance indicators (KPIs)
* Generates summary tables by product, category, and month
* Creates revenue visualizations
* Produces a text-based analysis report
* Includes automated tests with pytest
* Uses GitHub Actions for continuous testing

Quick start

pip install -r requirements.txt
python main.py

The generated reports, summary tables, and charts are saved in reports/.

Project structure

python-data-analysis/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── sales.csv
├── reports/
│   ├── category_summary.csv
│   ├── product_summary.csv
│   ├── monthly_summary.csv
│   ├── monthly_revenue.png
│   ├── revenue_by_category.png
│   └── report.txt
├── src/
│   ├── _init_.py
│   └── analysis.py
├── tests/
│   └── test_analysis.py
├── .gitignore
├── LICENSE
├── main.py
├── requirements.txt
└── README.md

Testing

Run the test suite with:

python -m pytest

The project also runs automated tests through GitHub Actions whenever changes are pushed or a pull request is opened.

Dataset

The included sales dataset is synthetic/demo data created for development, testing, and demonstration purposes. It does not represent real customers or real business transactions.

Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Pytest
* GitHub Actions

Purpose

This project demonstrates a reproducible workflow for transforming sales data into structured business reports, performance metrics, and visual insights
