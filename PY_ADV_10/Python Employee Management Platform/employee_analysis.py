import pandas as pd

# Read employee data
df = pd.read_csv("employees.csv")

# Handle missing values
df["salary"] = df["salary"].fillna(df["salary"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Filter employees with salary above 45000
df = df[df["salary"] > 45000]

# Save cleaned dataset
df.to_csv("clean_employees.csv", index=False)

print("Cleaned Employee Data:")
print(df)

# Basic employee statistics
print("\nEmployee Statistics:")
print("Total Employees:", len(df))
print("Average Salary:", df["salary"].mean())
print("Maximum Salary:", df["salary"].max())
print("Minimum Salary:", df["salary"].min())