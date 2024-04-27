import cv2

# Load the image
image = cv2.imread('F:\TY Sem 2\IPPR\Practicals\IPPR CODES\logo.jpg')


# Get the original image dimensions
height, width = image.shape[:2]

# Scale the image by a factor of 2
scaled_image_up = cv2.resize(image, (2 * width, 2 * height))

# Scale the image by a factor of 0.5
scaled_image_down = cv2.resize(image, (width // 2, height // 2))

# Scale the image by a factor of 1 (original size)
scaled_image_original = cv2.resize(image, (width, height))

# Display the scaled images
cv2.imshow('Scaled Image (Factor 2)', scaled_image_up)
cv2.imshow('Scaled Image (Factor 0.5)', scaled_image_down)
cv2.imshow('Scaled Image (Factor 1)', scaled_image_original)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
