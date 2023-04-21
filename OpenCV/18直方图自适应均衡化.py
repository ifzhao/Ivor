import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', flags=0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

plt.imshow(cl1, cmap=plt.cm.gray)
plt.show()
