import cv2
import matplotlib.pylab as plt
import numpy as np

img = np.zeros((128, 128, 3), np.uint8)
cv2.line(img, (3, 7), (93, 110), (255, 0, 0), 5)
cv2.rectangle(img, (6, 9), (66, 78), (152, 73, 0), 5)
plt.imshow(img[:, :, ::-1])
plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
plt.show()
