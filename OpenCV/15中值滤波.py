import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
img2 = cv2.medianBlur(img1, 5)
plt.imshow(img2[:, :, ::-1])
plt.show()
cv2.imwrite('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\medianblur.jpeg', img2)