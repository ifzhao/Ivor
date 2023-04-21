import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')

# plt.imshow(img1[:, :, ::-1])
# plt.show()

rows, cols = img1.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
img2 = cv2.warpAffine(img1, M, (cols,rows))

plt.imshow(img2[:, :, ::-1])
plt.show()
