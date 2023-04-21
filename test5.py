import os
import random
import matplotlib.pyplot as plt
from PIL import Image
import time

def main(path):
    file_path = path
    file_list = os.listdir(file_path)
    selected_file = random.choice(file_list)
    image = Image.open(os.path.join(file_path, selected_file))
    plt.imshow(image)
    plt.pause(1)
    plt.close()


if __name__ == '__main__':
    for i in range(600):
        print(i)
        main("C:/Users/ifzhao/Pictures/新建文件夹")
        # time.sleep()
