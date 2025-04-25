import pandas as pd

# Sample data
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create a pivot table
pivot_table = df.pivot_table(values='Sales', index='Date', columns='Category', aggfunc='sum', fill_value=0)

print("Original DataFrame:")
print(df)
print("\nPivot Table:")
print(pivot_table)