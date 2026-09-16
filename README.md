# Customer Churn Analysis

## 📌 Project Overview

Customer Churn Analysis is a Python data analysis project that analyzes customer information to understand patterns related to customer churn.

The project uses **Python, Pandas, Matplotlib, and Seaborn** to generate customer data, perform data analysis, calculate churn rates, and create visualizations.

## 🎯 Objectives

* Analyze customer churn and retention.
* Identify churn patterns based on contract type.
* Analyze churn based on internet service.
* Study the relationship between support calls and churn.
* Analyze customer tenure and monthly charges.
* Create visualizations to understand customer behavior.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* CSV
* VS Code

## 📂 Project Structure

```text
Customer_Churn_Analysis/
│
├── churn_analysis.py
├── README.md
│
└── data/
    ├── customer_churn.csv
    ├── customer_churn_cleaned.csv
    ├── churn_distribution.png
    ├── churn_by_contract.png
    ├── churn_by_internet.png
    ├── monthly_charges_vs_churn.png
    ├── tenure_vs_churn.png
    └── support_calls_vs_churn.png
```

## 📊 Dataset

The project uses a generated dataset containing **500 customer records**.

The dataset includes:

* Customer ID
* Gender
* Age
* Tenure
* Contract
* Monthly Charges
* Total Charges
* Internet Service
* Payment Method
* Support Calls
* Churn

## 📈 Key Results

* Total Customers: **500**
* Churned Customers: **168**
* Retained Customers: **332**
* Churn Rate: **33.6%**
* Retention Rate: **66.4%**
* Average Tenure: **33.15 months**
* Average Monthly Charge: **69.26**

### Contract Analysis

In this generated dataset:

* Monthly contract customers had a churn rate of **46.6%**.
* One Year contract customers had a churn rate of **28.5%**.
* Two Year contract customers had a churn rate of **27.8%**.

### Internet Service Analysis

* DSL: **31.2%** churn rate
* Fiber Optic: **37.8%** churn rate
* No Internet: **31.0%** churn rate

### Support Calls Analysis

Customers with **7 or more support calls** showed higher churn rates in this generated dataset.

### Tenure Analysis

The highest churn rate was observed in the **37–48 month** tenure group at **39.3%**.

> Note: This project uses a synthetic/generated dataset. Therefore, these findings represent patterns in this project dataset and should not be treated as real-world telecom industry conclusions.

## ▶️ How to Run

Make sure Python is installed on your system.

Run the following command:

```bash
python churn_analysis.py
```

The program generates the CSV files and visualization charts inside the `data` folder.

## 📊 Visualizations

The project generates charts for:

* Churn Distribution
* Churn by Contract
* Churn by Internet Service
* Monthly Charges vs Churn
* Tenure vs Churn
* Support Calls vs Churn

## 🚀 Future Improvements

* Create an interactive Power BI dashboard.
* Add more customer behavior analysis.
* Build a machine learning model to predict customer churn.
* Add additional visualizations and KPIs.

## 👩‍💻 Author

**Reshma Dudekula**

B.Tech – Electronics & Communication Engineering
