import cv2

def edge_detection_sobel(input_image_path):
    # Read the image
    img = cv2.imread(input_image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Sobel operator in the x and y directions
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calculate the gradient magnitude
    gradient_magnitude = cv2.magnitude(sobelx, sobely)
    
    # Normalize the gradient magnitude to 0-255
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    
    # Apply thresholding to obtain a binary image
    _, edges = cv2.threshold(gradient_magnitude_normalized, 50, 255, cv2.THRESH_BINARY)
    
    # Display the original and segmented images
    cv2.imshow('Original Image', img)
    cv2.imshow('Edge Detection using Sobel Operator', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = "F:\TY Sem 2\IPPR\Practicals\IPPR CODES\logo.jpg"
edge_detection_sobel(input_image_path)
