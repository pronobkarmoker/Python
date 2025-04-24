from PIL import Image
import numpy as np

# Load the image
image_path = "python.jpg"  # Replace with your image path
image = Image.open(image_path)

# Convert the image to a NumPy array (matrix)
image_matrix = np.array(image)

# Invert the colors to create a dark mode effect
dark_mode_matrix = 255 - image_matrix

# Convert the matrix back to an image
dark_mode_image = Image.fromarray(dark_mode_matrix)

# Save the dark mode image
dark_mode_image.save("dark_mode_image.jpg")
print("Dark mode image saved as 'dark_mode_image.jpg'")