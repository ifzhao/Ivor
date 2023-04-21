import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
img2 = cv2.imread("C:\\Users\\ifzhao\\Pictures\\tu.jpg")

rows1, cols1 = img1.shape[:2]
rows2, cols2 = img2.shape[:2]
print(rows1, cols1, rows2, cols2)

img3 = cv2.resize(img1, (rows2 * rows1, cols2 * cols1))
img4 = cv2.resize(img2, (rows1 * rows2, cols1 * cols2))
img5 = img3 + img4
plt.imshow(img3[:, :, ::-1])
plt.show()
