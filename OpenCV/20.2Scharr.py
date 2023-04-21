import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg', flags=0)

# 计算Soble卷积结果
x = cv2.Sobel(img, cv2.CV_16S, 1, 0,ksize= -1)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1,ksize= -1)

# 将数据进行转换
Scale_absX = cv2.convertScaleAbs(x)
Scale_absY = cv2.convertScaleAbs(y)

# 结果合成
result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)

# 展示图像
plt.imshow(result)
plt.show()