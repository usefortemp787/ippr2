from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def negative_image(inp_img_path):
    img = Image.open(inp_img_path)
    img = img.convert('RGB')  # Convert the image to RGB mode
    width, height = img.size
    neg_img = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))  
            neg_r = 255 - r
            neg_g = 255 - g
            neg_b = 255 - b

            neg_img.putpixel((i, j), (neg_r, neg_g, neg_b))  
    img_arr = np.array(img)
    neg_img_arr = np.array(neg_img)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(neg_img)
    plt.title('Negative Image')
    plt.axis('off')

    plt.show()


negative_image(r"F:\\TY Sem 2\\IPPR\\Practicals\\IPPR CODES\\logo.jpg")
