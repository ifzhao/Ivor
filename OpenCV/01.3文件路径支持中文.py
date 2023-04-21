import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imdecode(np.fromfile("E:/图片/汽车.jpg", dtype=np.uint8), 1)

cv2.imshow("img", img)
cv2.imencode('.jpg', img)[1].tofile("E:/图片/汽车备份.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
