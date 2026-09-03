import pandas as pd

# Read CSV
df = pd.read_csv("employees.csv")

# Handle missing values
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Filter data
df = df[df["Salary"] > 45000]

# Save clean dataset
df.to_csv("clean_employees.csv", index=False)

print("Cleaned Employee Data:")
print(df)