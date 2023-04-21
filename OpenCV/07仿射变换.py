import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')

# plt.imshow(img1[:, :, ::-1])
# plt.show()

rows, cols = img1.shape[:2]
pts1 = np.float32([1000, 1000], [2000, 2000], [1000, 2000])
pts2 = np.float32([1000, 1000], [2000, 2000], [1000, 2000])

M = cv2.getRotationMatrix2D(pts1, pts2)
img2 = cv2.warpAffine(img1, M, (cols, rows))

plt.imshow(img2[:, :, ::-1])
plt.show()
