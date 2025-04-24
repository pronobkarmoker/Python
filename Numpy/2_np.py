import numpy as np

# Create larger arrays
arr1 = np.array([1, 2, 3, 4, 5, 6])  # Increased size
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Larger 2D array

# Array properties
print(arr1.shape)  # Shape of the array
print(arr2.ndim)   # Number of dimensions
print(arr1.size)   # Total number of elements
print(arr1.dtype)  # Data type of elements

# Array creation
zeros = np.zeros((2, 3))  # Array of zeros
ones = np.ones((3, 2))    # Array of ones
identity = np.eye(3)      # Identity matrix
arange = np.arange(0, 10, 2)  # Array with a range
linspace = np.linspace(0, 1, 5)  # Array with evenly spaced values

# Reshaping
reshaped = arr1.reshape((2, 3))

# Indexing and slicing
print(arr2[0, 1])  # Access element
print(arr2[:, 1])  # Access column
print(arr2[0, :])  # Access row

# Mathematical operations
print(arr1 + 2)  # Add scalar
print(arr1 * 3)  # Multiply scalar
print(arr1 + arr1)  # Add arrays
print(arr1 * arr1)  # Element-wise multiplication
print(np.dot(arr1, arr1))  # Dot product

# Aggregate functions
print(np.sum(arr2))  # Sum of all elements
print(np.mean(arr2))  # Mean of all elements
print(np.min(arr2))  # Minimum value
print(np.max(arr2))  # Maximum value
print(np.std(arr2))  # Standard deviation

# Transpose
print(arr2.T)

# Stacking
stacked = np.vstack((arr1, arr1))  # Vertical stack
stacked = np.hstack((arr1, arr1))  # Horizontal stack

# Splitting
split = np.split(arr1, 2)

# Logical operations
print(arr1 > 2)  # Element-wise comparison
print(np.any(arr1 > 2))  # Check if any element satisfies condition
print(np.all(arr1 > 0))  # Check if all elements satisfy condition

# Copying
arr_copy = arr1.copy()

# Broadcasting
broadcasted = arr1 + np.array([1, 2, 3, 4, 5, 6])

# Advanced indexing
indices = [0, 2, 4]
print(arr1[indices])  # Access specific indices

# Sorting operations
sorted_arr = np.sort(arr1)  # Sort array
sorted_indices = np.argsort(arr1)  # Indices of sorted elements
sorted_2d = np.sort(arr2, axis=0)  # Sort along columns
sorted_2d_row = np.sort(arr2, axis=1)  # Sort along rows

print(sorted_arr)
print(sorted_indices)
print(sorted_2d)
print(sorted_2d_row)

# Array filtering
filtered = arr1[arr1 > 3]  # Filter elements greater than 3
print(filtered)

filtered_2d = arr2[arr2 % 2 == 0]  # Filter even elements in 2D array
print(filtered_2d)
# Using np.where for conditional selection
condition = arr1 > 3
result_where = np.where(condition, arr1, -1)  # Replace elements not satisfying condition with -1
print(result_where)

# Fancy indexing for conditional selection
fancy_indexed = arr1[arr1 > 3]  # Directly filter elements greater than 3
print(fancy_indexed)

# More examples of np.where()
# Replace elements less than 4 with 0
modified_arr1 = np.where(arr1 < 4, 0, arr1)
print(modified_arr1)

# Replace even numbers with -1 and odd numbers with 1
modified_arr2 = np.where(arr2 % 2 == 0, -1, 1)
print(modified_arr2)

# Use np.where with multiple conditions
modified_arr1_multiple = np.where((arr1 > 2) & (arr1 < 5), 10, arr1)
print(modified_arr1_multiple)

# Replace elements based on condition in a 2D array
modified_arr2_2d = np.where(arr2 > 5, 99, arr2)
print(modified_arr2_2d)