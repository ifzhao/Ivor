import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')

kernel = np.ones((10, 10), np.uint8)

# imgtophat = cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,kernel)
imgblackhat = cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,kernel)

# plt.imshow(imgtophat[:, :, ::-1])
plt.imshow(imgblackhat[:, :, ::-1])
plt.show()