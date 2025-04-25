import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['shuvo', 'dip', 'barua'],
    'Age': [25, 30, 35],
    'City': ['gaibandha', 'jamalpur', 'coxsbazar'],
    'Country': ['Bangladesh', 'Bangladesh', 'Bangladesh']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Accessing a column
print("\nAccessing 'Name' column:")
print(df['Name'])

# Accessing a row by index
print("\nAccessing first row:")
print(df.iloc[0])

# Displaying the first few rows of the DataFrame
print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

# Displaying the last few rows of the DataFrame
print("\nLast 2 rows of the DataFrame:")
print(df.tail(2))

# Displaying information about the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())

# Displaying summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())

# Filtering data
print("\nFiltering rows where Age > 30:")
print(df[df['Age'] > 30])

# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# Saving to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'")