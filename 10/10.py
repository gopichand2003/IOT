import cv2
import numpy as np
img = cv2.imread('./photo-1503023345310-bd7c1de61c7d.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = np.ones((5,5),np.uint8)
dilated = cv2.dilate(edges, kernel, iterations = 1)
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
plt.imshow(gray)
plt.show()
plt.imshow(blur)
plt.show()
plt.imshow(edges)
plt.show()
plt.imshow(dilated)
plt.show()
