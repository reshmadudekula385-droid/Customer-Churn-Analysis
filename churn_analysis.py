# ============================================================
# CUSTOMER CHURN ANALYSIS
# Python + Pandas + Matplotlib + Seaborn
# ============================================================

import pandas as pd
import random
import os
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. CREATE CUSTOMER DATA
# ============================================================

print("=" * 60)
print("CUSTOMER CHURN ANALYSIS")
print("=" * 60)

random.seed(42)

customers = []

for i in range(1, 501):

    customer_id = f"C{i:04d}"

    gender = random.choice(["Male", "Female"])

    age = random.randint(18, 65)

    tenure = random.randint(1, 60)

    contract = random.choice([
        "Monthly",
        "One Year",
        "Two Year"
    ])

    monthly_charges = round(random.uniform(20, 120), 2)

    total_charges = round(monthly_charges * tenure, 2)

    internet_service = random.choice([
        "DSL",
        "Fiber Optic",
        "No"
    ])

    payment_method = random.choice([
        "Credit Card",
        "Debit Card",
        "Bank Transfer",
        "UPI"
    ])

    support_calls = random.randint(0, 10)

    # Calculate churn probability

    churn_probability = 0.15

    if contract == "Monthly":
        churn_probability += 0.20

    if tenure < 12:
        churn_probability += 0.15

    if support_calls >= 7:
        churn_probability += 0.15

    if monthly_charges > 90:
        churn_probability += 0.10

    if random.random() < churn_probability:
        churn = "Yes"
    else:
        churn = "No"

    customers.append([
        customer_id,
        gender,
        age,
        tenure,
        contract,
        monthly_charges,
        total_charges,
        internet_service,
        payment_method,
        support_calls,
        churn
    ])


# ============================================================
# 2. CREATE DATAFRAME
# ============================================================

columns = [
    "CustomerID",
    "Gender",
    "Age",
    "Tenure",
    "Contract",
    "MonthlyCharges",
    "TotalCharges",
    "InternetService",
    "PaymentMethod",
    "SupportCalls",
    "Churn"
]

df = pd.DataFrame(customers, columns=columns)


# ============================================================
# 3. CREATE DATA FOLDER
# ============================================================

if not os.path.exists("../data"):
    os.makedirs("../data")


# ============================================================
# 4. SAVE ORIGINAL DATASET
# ============================================================

df.to_csv(
    "../data/customer_churn.csv",
    index=False
)

print("\nDataset created successfully!")


# ============================================================
# 5. DISPLAY FIRST 5 ROWS
# ============================================================

print("\n" + "=" * 60)
print("FIRST 5 CUSTOMERS")
print("=" * 60)

print(df.head())


# ============================================================
# 6. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("Total Customers:", len(df))
print("Total Columns:", len(df.columns))

print("\nColumn Names:")

for column in df.columns:
    print(column)


# ============================================================
# 7. CHECK MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# 8. CHECK DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print("Duplicates:", df.duplicated().sum())


# ============================================================
# 9. DATA TYPES
# ============================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# ============================================================
# 10. BASIC STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print(df.describe())


# ============================================================
# 11. TOTAL CUSTOMERS
# ============================================================

total_customers = len(df)

print("\nTotal Customers:", total_customers)


# ============================================================
# 12. CHURN COUNT
# ============================================================

churn_count = df["Churn"].value_counts()

print("\n" + "=" * 60)
print("CHURN COUNT")
print("=" * 60)

print(churn_count)


# ============================================================
# 13. CHURNED CUSTOMERS
# ============================================================

churned_customers = len(
    df[df["Churn"] == "Yes"]
)

print("\nChurned Customers:", churned_customers)


# ============================================================
# 14. RETAINED CUSTOMERS
# ============================================================

retained_customers = len(
    df[df["Churn"] == "No"]
)

print("Retained Customers:", retained_customers)


# ============================================================
# 15. CHURN RATE
# ============================================================

churn_rate = (
    churned_customers / total_customers
) * 100

print("\nChurn Rate:", round(churn_rate, 2), "%")


# ============================================================
# 16. RETENTION RATE
# ============================================================

retention_rate = (
    retained_customers / total_customers
) * 100

print("Retention Rate:", round(retention_rate, 2), "%")


# ============================================================
# 17. GENDER-WISE CHURN
# ============================================================

print("\n" + "=" * 60)
print("GENDER-WISE CHURN")
print("=" * 60)

gender_churn = pd.crosstab(
    df["Gender"],
    df["Churn"]
)

print(gender_churn)


# ============================================================
# 18. CONTRACT-WISE CHURN
# ============================================================

print("\n" + "=" * 60)
print("CONTRACT-WISE CHURN")
print("=" * 60)

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print(contract_churn)


# ============================================================
# 19. INTERNET SERVICE-WISE CHURN
# ============================================================

print("\n" + "=" * 60)
print("INTERNET SERVICE-WISE CHURN")
print("=" * 60)

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

print(internet_churn)


# ============================================================
# 20. PAYMENT METHOD-WISE CHURN
# ============================================================

print("\n" + "=" * 60)
print("PAYMENT METHOD-WISE CHURN")
print("=" * 60)

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print(payment_churn)


# ============================================================
# 21. AVERAGE MONTHLY CHARGES
# ============================================================

average_monthly_charges = df[
    "MonthlyCharges"
].mean()

print("\nAverage Monthly Charges:",
      round(average_monthly_charges, 2))


# ============================================================
# 22. AVERAGE TENURE
# ============================================================

average_tenure = df["Tenure"].mean()

print("Average Tenure:",
      round(average_tenure, 2),
      "months")


# ============================================================
# 23. TENURE GROUP
# ============================================================

df["TenureGroup"] = pd.cut(
    df["Tenure"],
    bins=[0, 12, 24, 36, 48, 60],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-36 Months",
        "37-48 Months",
        "49-60 Months"
    ]
)


# ============================================================
# 24. TENURE-WISE CHURN
# ============================================================

print("\n" + "=" * 60)
print("TENURE-WISE CHURN")
print("=" * 60)

tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"]
)

print(tenure_churn)


# ============================================================
# 25. SUPPORT CALLS VS CHURN
# ============================================================

print("\n" + "=" * 60)
print("SUPPORT CALLS VS CHURN")
print("=" * 60)

support_churn = pd.crosstab(
    df["SupportCalls"],
    df["Churn"]
)

print(support_churn)


# ============================================================
# 26. HIGH CHARGE CHURNED CUSTOMERS
# ============================================================

high_charge_churn = df[
    (df["Churn"] == "Yes") &
    (df["MonthlyCharges"] > 90)
]

print("\n" + "=" * 60)
print("HIGH CHARGE CHURNED CUSTOMERS")
print("=" * 60)

print(high_charge_churn.head(10))


# ============================================================
# 27. SAVE CLEANED DATASET
# ============================================================

df.to_csv(
    "data/customer_churn_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")


# ============================================================
# 28. CHART 1 - CHURN DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Churn"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "data/churn_distribution.png"
)

plt.show()


# ============================================================
# 29. CHART 2 - CONTRACT VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn"
)

plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "data/churn_by_contract.png"
)

plt.show()


# ============================================================
# 30. CHART 3 - INTERNET SERVICE VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="InternetService",
    hue="Churn"
)

plt.title("Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "data/churn_by_internet.png"
)

plt.show()


# ============================================================
# 31. CHART 4 - MONTHLY CHARGES VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)

plt.title("Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.tight_layout()

plt.savefig(
    "data/monthly_charges_vs_churn.png"
)

plt.show()


# ============================================================
# 32. CHART 5 - TENURE VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="Tenure"
)

plt.title("Tenure vs Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure in Months")

plt.tight_layout()

plt.savefig(
    "data/tenure_vs_churn.png"
)

plt.show()


# ============================================================
# 33. CHART 6 - SUPPORT CALLS VS CHURN
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="SupportCalls"
)

plt.title("Support Calls vs Churn")
plt.xlabel("Churn")
plt.ylabel("Number of Support Calls")

plt.tight_layout()

plt.savefig(
    "data/support_calls_vs_churn.png"
)

plt.show()


# ============================================================
# 34. FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 60)
print("FINAL CUSTOMER CHURN SUMMARY")
print("=" * 60)

print("Total Customers        :", total_customers)
print("Churned Customers      :", churned_customers)
print("Retained Customers     :", retained_customers)
print("Churn Rate             :", round(churn_rate, 2), "%")
print("Retention Rate         :", round(retention_rate, 2), "%")
print("Average Tenure         :", round(average_tenure, 2), "months")
print("Average Monthly Charge :", round(average_monthly_charges, 2))

print("=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)