import numpy as np
import matplotlib.pyplot as plt

# Real-world data: Monthly temperatures (in Celsius) of a city for 3 years
temperatures = np.array([
    [3.2, 4.5, 8.9, 13.2, 18.3, 22.5, 25.6, 24.8, 20.1, 14.2, 8.3, 4.1],  # Year 1
    [2.8, 4.0, 9.1, 12.8, 17.9, 21.9, 25.0, 24.5, 19.8, 13.8, 7.9, 3.8],  # Year 2
    [3.5, 4.8, 9.3, 13.5, 18.5, 22.8, 26.0, 25.0, 20.5, 14.5, 8.5, 4.3]   # Year 3
])


# 1. Basic statistics for all years
mean_temp = np.mean(temperatures)  # Overall average temperature
median_temp = np.median(temperatures)  # Overall median temperature
std_temp = np.std(temperatures)  # Overall standard deviation
max_temp = np.max(temperatures)  # Overall maximum temperature
min_temp = np.min(temperatures)  # Overall minimum temperature

# 2. Yearly statistics
yearly_mean = np.mean(temperatures, axis=1)  # Mean temperature per year
yearly_max = np.max(temperatures, axis=1)  # Max temperature per year
yearly_min = np.min(temperatures, axis=1)  # Min temperature per year

# 3. Monthly average across years
monthly_mean = np.mean(temperatures, axis=0)

# 4. Temperature conversion (Celsius to Fahrenheit)
temperatures_fahrenheit = temperatures * 9/5 + 32

# 5. Filtering temperatures above 20°C
above_20 = temperatures[temperatures > 20]

# 6. Adding a constant to all temperatures (e.g., global warming effect)
adjusted_temperatures = temperatures + 1.5

# 7. Sorting temperatures for each year
sorted_temperatures = np.sort(temperatures, axis=1)

# 8. Difference between consecutive months for each year
monthly_diff = np.diff(temperatures, axis=1)

# Print results
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Standard Deviation:", std_temp)
print("Max Temperature:", max_temp)
print("Min Temperature:", min_temp)
print("Yearly Mean Temperatures:", yearly_mean)
print("Yearly Max Temperatures:", yearly_max)
print("Yearly Min Temperatures:", yearly_min)
print("Monthly Mean Temperatures Across Years:", monthly_mean)
print("Temperatures in Fahrenheit:\n", temperatures_fahrenheit)
print("Temperatures above 20°C:", above_20)
print("Adjusted Temperatures:\n", adjusted_temperatures)
print("Sorted Temperatures:\n", sorted_temperatures)
print("Monthly Differences:\n", monthly_diff)

# Matplotlib operations for visualization

# 1. Plot yearly temperatures
for i, year in enumerate(temperatures, start=1):
    plt.plot(range(1, 13), year, label=f'Year {i}')
plt.title('Monthly Temperatures Over 3 Years')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Plot monthly average temperatures
plt.plot(range(1, 13), monthly_mean, marker='o', color='red', label='Monthly Average')
plt.title('Monthly Average Temperatures Across Years')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

# 3. Histogram of all temperatures
plt.hist(temperatures.flatten(), bins=10, color='blue', edgecolor='black')
plt.title('Histogram of Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()