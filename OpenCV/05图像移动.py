import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')

plt.imshow(img1[:,:,::-1])
plt.show()

rows, cols = img1.shape[:2]
M = np.float32([[1, 0, 1000], [0, 1, 500]])
img2 = cv2.warpAffine(img1, M, (2*rows, 2*cols))

plt.imshow(img2[:,:,::-1])
plt.show()

