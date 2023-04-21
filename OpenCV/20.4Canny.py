import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', flags=0)
low = 0
mlow = 100
canny = cv2.Canny(img,low,mlow)

plt.imshow(canny)
plt.show()