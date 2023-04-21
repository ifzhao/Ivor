import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', flags=0)
result = cv2.Laplacian(img,cv2.CV_16S)
Scale_abs = cv2.convertScaleAbs(result)

plt.imshow(Scale_abs)
plt.show()