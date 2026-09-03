import pandas as pd

# Read employee data
df = pd.read_csv("employees.csv")

# Data cleaning
cleaned_df = df.drop_duplicates()
cleaned_df = cleaned_df.dropna()

# Display employee data
print("Employee Data:")
print(cleaned_df)

# Basic statistics
print("\nAverage Salary:", cleaned_df["Salary"].mean())
print("Median Salary:", cleaned_df["Salary"].median())

# Highest salary
print("\nHighest Salary:")
print(cleaned_df.loc[cleaned_df["Salary"].idxmax()])

# Lowest salary
print("\nLowest Salary:")
print(cleaned_df.loc[cleaned_df["Salary"].idxmin()])

# Department-wise average salary
print("\nAverage Salary by Department:")
print(cleaned_df.groupby("Department")["Salary"].mean())

# Save cleaned data
cleaned_df.to_csv("cleaned_employees.csv", index=False)

print("\nCleaned CSV file saved successfully.")