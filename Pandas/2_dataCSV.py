import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('data.csv')
print(df)   

# Check for missing values
print("Missing values in each column:")
print(df.isnull())
print(df.isnull().sum())

# Fill missing values with the mean of the column
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert a specific column to the correct data type (example: 'Date' column to datetime)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

print("\nSummary statistics of the DataFrame:")
print(df.describe())

df.to_excel('output.xlsx', index=False)
print("\nDataFrame saved to 'output.xlsx'")


# # Plot the data using matplotlib
# if 'Date' in df.columns and 'Value' in df.columns:
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='b', label='Value over Time')
#     plt.xlabel('Date')
#     plt.ylabel('Value')
#     plt.title('Value vs Date')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
# else:
#     print("The required columns 'Date' and 'Value' are not present in the DataFrame.")
