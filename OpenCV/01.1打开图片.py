import cv2
import matplotlib.pylab as plt
import numpy as np
img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
# cv2.imwrite('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\gray.jpeg',img)






