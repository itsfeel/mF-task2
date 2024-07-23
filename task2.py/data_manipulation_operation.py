import pandas as pd

data_cleaned = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
    'Age': [29, 34, 28.25, 32, 28],
    'Salary': [70000, 80000, 65000, 77000, 72000],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT']
}

df_no_duplicates = pd.DataFrame(data_cleaned)
print("\nDataFrame for Data Manipulation:")
print(df_no_duplicates)

filtered_df = df_no_duplicates[df_no_duplicates['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

sorted_df = df_no_duplicates.sort_values(by='Salary', ascending=False)
print("\nDataFrame Sorted by Salary (Descending):")
print(sorted_df)

grouped_df = df_no_duplicates.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(grouped_df)