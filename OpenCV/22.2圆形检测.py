import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 读取图像，并转换为灰度图
planets = cv.imread("C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg")
gay_img = cv.cvtColor(planets, cv.COLOR_BGRA2GRAY)
# 2 进行中值模糊，去噪点
img = cv.medianBlur(gay_img, 7)
# 3 霍夫圆检测
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=30, minRadius=0, maxRadius=100)
# 4 将检测结果绘制在图像上
for i in circles[0, :]:  # 遍历矩阵每一行的数据
    # 绘制圆形
    cv.circle(planets, i[0], i[1], i[2], (0, 255, 0), 2)
    # 绘制圆心
    cv.circle(planets, i[0], i[1], 2, (0, 0, 255), -1)
# 5 图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(planets[:, :, ::-1]), plt.title('result')
plt.xticks([]), plt.yticks([])
plt.show()
