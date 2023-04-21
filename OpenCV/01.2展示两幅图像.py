import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
img2 = cv2.imread("C:\\Users\\ifzhao\\Pictures\\tu.jpg")

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0,0].imshow(img1[:,:,::-1])
axes[0,0].set_title("图1标题")
axes[0,1].imshow(img2[:,:,::-1])
axes[0,1].set_title("图2标题")
plt.show()
