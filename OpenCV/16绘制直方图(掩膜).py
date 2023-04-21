import matplotlib.pyplot as plt
import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', 0)

# 创建模板
mask = np.zeros(img1.shape[:2], np.uint8)
mask[1000:6000, 1000:4000] = 255

# 掩膜
mask_img = cv2.bitwise_and(img1, img1, mask=mask)

histr = cv2.calcHist([img1], [0], mask_img, [256], [0, 256])
plt.imshow(mask_img, cmap=plt.cm.gray)
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr)
plt.gray()
plt.show()
