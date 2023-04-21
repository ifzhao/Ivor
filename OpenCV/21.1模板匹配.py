import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('C:\\Users\\ifzhao\\Pictures\\shuai_flie\\1635587860094.jpeg')
template = cv2.imread("C:\\Users\\ifzhao\\Pictures\\tu.jpg")
h, w = template.shape[:2]

# 匹配模板
res = cv2.matchTemplate(img, template, cv2.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 0)

# 显示图像
plt.imshow(img[:, :, ::-1])
plt.title("result"), plt.xticks([]), plt.yticks([])
plt.show()
