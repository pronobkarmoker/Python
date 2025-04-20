import numpy as np
import time
# Create a 1D array with 5 elements
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)
# Create a 2D array (matrix) with 3 rows and 4 columns
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("2D Array:\n", arr_2d)
# Create a 3D array with shape (2, 3, 4)
arr_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
print("3D Array:\n", arr_3d)
# Create an array of zeros with shape (2, 3)
arr_zeros = np.zeros((2, 3))
print("Array of Zeros:\n", arr_zeros)  
# Create an array of ones with shape (3, 4)
arr_ones = np.ones((3, 4))
print("Array of Ones:\n", arr_ones)
#full matrix
arr_full = np.full((2, 3), 7)  # Fill with the value 7 
print("Full Array:\n", arr_full)
# Create an identity matrix of size 3x3
arr_identity = np.eye(3)
print("Identity Matrix:\n", arr_identity)
# Create an array with random values of shape (2, 2)
arr_random = np.random.rand(2, 2)
print("Random Array:\n", arr_random)
# Create an array with a range of values from 0 to 9
arr_range = np.arange(10)
print("Array with Range:\n", arr_range)
# Create an array with evenly spaced values from 0 to 1 with 5 elements
arr_linspace = np.linspace(0, 1, 5)
print("Array with Linspace:\n", arr_linspace)
# Reshape the 1D array to a 2D array with shape (5, 1)
arr_reshaped = arr_1d.reshape(5, 1)
print("Reshaped Array:\n", arr_reshaped)
# Transpose the 2D array
arr_transposed = arr_2d.T   


# Create a Python list and a NumPy array with the same elements
list_data = [i*2 for i in range(1, 10001)]
numpy_data = np.array(list_data)

# Measure time for multiplying each element in the list by 2
start_time = time.time()
list_result = [x * 2 for x in list_data]
list_time = time.time() - start_time
print("Time taken for list multiplication:", list_time)

# Measure time for multiplying each element in the NumPy array by 2
start_time = time.time()
numpy_result = numpy_data * 2
numpy_time = time.time() - start_time
print("Time taken for NumPy array multiplication:", numpy_time)

# Compare the results
print("List multiplication result (first 5 elements):", list_result[:5])
print("NumPy array multiplication result (first 5 elements):", numpy_result[:5])

#tensor
tensor = np.array([[[[[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]]]]])
print("Tensor:\n", tensor)
#tensor shape
print("Tensor shape:", tensor.shape)
#tensor reshape
tensor_reshaped = tensor.reshape(2, 3, 2, 1)
print("Reshaped Tensor:\n", tensor_reshaped)