import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_dataset.csv")

# Standardize categories
df["Performance_Score"] = df["Performance_Score"].astype(str).str.strip().str.title()
df["Join_Date"] = pd.to_datetime(df["Join_Date"], dayfirst=True, errors="coerce")

print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

print("\nDepartment counts:\n", df["Department"].value_counts())
print("\nRegion counts:\n", df["Region"].value_counts())
print("\nPerformance counts:\n", df["Performance_Score"].value_counts())
print("\nRemote work:\n", df["Remote_Work"].value_counts())

print("\nAverage salary:", round(df["Salary"].mean(), 2))
print("Average age:", round(df["Age"].mean(), 2))

dept_salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print("\nAverage salary by department:\n", dept_salary)

year_counts = df.groupby(df["Join_Date"].dt.year).size()
print("\nEmployees by joining year:\n", year_counts)

# Example visualizations
df["Department"].value_counts().plot(kind="bar", title="Employees by Department")
plt.tight_layout()
plt.show()

sns.countplot(data=df, x="Performance_Score", order=["Good", "Average", "Excellent", "Poor"])
plt.title("Employee Performance Distribution")
plt.tight_layout()
plt.show()
