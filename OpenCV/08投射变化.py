import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
plt.imshow(img[:,:,::-1])
plt.show()

rows,cols = img.shape[:2]
plt1 = np.float32()
plt2 = np.float32()
T = cv2.getPerspectiveTransform(plt1,plt2)
img2 = cv2.warpPerspective(img1,T,(cols,rows))



