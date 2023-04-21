import cv2
import matplotlib.pylab as plt
import numpy as np

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', 0)

img2 = cv2.equalizeHist(img1)

plt.imshow(img2,cmap=plt.cm.gray)
plt.show()
