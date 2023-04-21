import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', flags=0)
# gray = cv2.cvtColor(img)
canny = cv2.Canny(img, 0, 100)
# 霍夫直线变换
lines = cv2.HoughLines(canny, 0.8, np.pi / 100, 150)
# 将检测的线绘制在图像上
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0))

plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img, cmap=plt.cm.gray), plt.title("ruselt")
plt.xticks([]), plt.yticks([])
plt.show()
