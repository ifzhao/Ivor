import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')

kernel = np.ones((10, 10), np.uint8)

# imgOpen = cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)
imgCloes = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)

# plt.imshow(imgOpen[:, :, ::-1])
plt.imshow(imgCloes[:, :, ::-1])
plt.show()