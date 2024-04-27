import cv2
import matplotlib.pyplot as plt
import numpy as np

def plot_rgb_histogram(img, title):
    # Split the image into RGB channels
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # Calculate histograms for each channel
    hist_r, bins = np.histogram(r.flatten(), bins=256, range=[0,256])
    hist_g, _ = np.histogram(g.flatten(), bins=256, range=[0,256])
    hist_b, _ = np.histogram(b.flatten(), bins=256, range=[0,256])
    
    # Plot the histograms
    plt.figure(figsize=(12, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(hist_r, color='r')
    plt.title(f'Red Channel {title} Histogram')
    plt.xlim([0, 256])
    
    plt.subplot(3, 1, 2)
    plt.plot(hist_g, color='g')
    plt.title(f'Green Channel {title} Histogram')
    plt.xlim([0, 256])
    
    plt.subplot(3, 1, 3)
    plt.plot(hist_b, color='b')
    plt.title(f'Blue Channel {title} Histogram')
    plt.xlim([0, 256])
    
    plt.tight_layout()
    plt.show()

def histogram_equalization(input_image_path):
    # Read the image
    img = cv2.imread(input_image_path)
    
    # Convert the image to YUV color space
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    
    # Equalize the histogram of the Y channel
    yuv_img[:,:,0] = cv2.equalizeHist(yuv_img[:,:,0])
    
    # Convert the image back to RGB
    equalized_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    
    # Plot the original and equalized image histograms
    plot_rgb_histogram(img, 'Original')
    plot_rgb_histogram(equalized_img, 'Equalized')
    
    # Display the original and equalized images
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(equalized_img, cv2.COLOR_BGR2RGB))
    plt.title('Equalized Image')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Example usage
input_image_path = 'F:\TY Sem 2\IPPR\Practicals\IPPR CODES\logo.jpg'
histogram_equalization(input_image_path)
