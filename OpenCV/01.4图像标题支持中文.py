
import cv2
import numpy as np


def zh_ch(string):
    return string.encode("gbk").decode(errors="ignore")


img = cv2.imdecode(np.fromfile("E:/图片/汽车.jpg", dtype=np.uint8), 1)
cv2.imshow(zh_ch('图片'), img)
cv2.imencode('.jpg', img)[1].tofile("E:/图片/汽车备份.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
