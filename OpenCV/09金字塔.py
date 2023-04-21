import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
# img2 = cv2.pyrUp(img1)
# plt.imshow(img2[:,:,::-1])
# plt.show()

img3 = cv2.pyrDown(img1)
plt.imshow(img3[:,:,::-1])
plt.show()