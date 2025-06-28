import cv2
import numpy as np
import matplotlib.pyplot as plt

def cartoonify_image(img_path):
    # Read image
    img = cv2.imread(img_path)
    img = cv2.resize(img, (800, 800))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 1. Edge Detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # 2. Color Smoothing
    color = cv2.bilateralFilter(img, d=9, sigmaColor=250, sigmaSpace=250)

    # 3. Combine edges and color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Show results
    titles = ['Original', 'Edge Map', 'Cartoon']
    images = [img_rgb, edges, cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)]

    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Example
cartoonify_image('your_image.jpg')
