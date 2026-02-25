import pandas as pd
import openpyxl 

data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'City': ['New York', 'London', 'Paris', 'London', 'New York', 'Paris', 'London', 'New York'],
    'Education_Level': ['High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'High School', 'Master', 'Bachelor'],
    'Experience_Level': ['Entry', 'Mid', 'Senior', 'Senior', 'Entry', 'Mid', 'Entry', 'Mid'],
    'Marks': [85, 70, 95, 60, 78, 88, 92, 65],
    'Status': ['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail']
}

df = pd.DataFrame(data)

# Save to Excel (Make sure you have 'openpyxl' installed: pip install openpyxl)
df.to_excel('student_practice.xlsx', index=False)
print("File 'student_practice.xlsx' created successfully!")