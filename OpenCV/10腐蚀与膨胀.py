import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Documents\\py_project\\window_pj\\new_image.png')

kernel = np.ones((15, 15), np.uint8)

img2 = cv2.erode(img1, kernel)
# img3 = cv2.dilate(img1, kernel)

plt.imshow(img2[:, :, ::-1])
# plt.imshow(img3[:, :, ::-1])
plt.show()
