import pandas as pd

data_with_issues = {
    'EmployeeID': [101, 102, 103, 104, 105, 101],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Rahul'],
    'Age': [29, 34, None, 32, 28, 29],
    'Salary': [70000, 80000, 65000, None, 72000, 70000],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT', 'IT']
}

df_with_issues = pd.DataFrame(data_with_issues)
print("\nDataFrame with Missing Values and Duplicates:")
print(df_with_issues)

df_cleaned = df_with_issues.fillna({
    'Age': df_with_issues['Age'].mean(),
    'Salary': df_with_issues['Salary'].mean()
})
print("\nDataFrame after Handling Missing Values:")
print(df_cleaned)

df_no_duplicates = df_cleaned.drop_duplicates()
print("\nDataFrame after Removing Duplicates:")
print(df_no_duplicates)
