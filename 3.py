from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def negative_image(inp_img_path) : 
    img = Image.open(inp_img_path)
    img_arr = np.array(img)
    neg_img_arr = 255 - img_arr
    neg_img = Image.fromarray(neg_img_arr)
    
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(neg_img, cmap='gray')
    plt.title('Negative Image')
    plt.axis('off')
    
    plt.show()
    
    return neg_img

negative_result = negative_image("F:\TY Sem 2\IPPR\Practicals\IPPR CODES\logo.jpg")


    