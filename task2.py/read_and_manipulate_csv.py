import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
    'Age': [29, 34, 22, 32, 28],
    'Salary': [70000, 80000, 65000, 90000, 72000],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
