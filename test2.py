import os
import random
import time
from PIL import Image
import tkinter as tk


def show_image(image_path, delay_time):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: root.quit())

    image = Image.open(image_path)
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()

    if image.width > width or image.height > height:
        if image.width / image.height > width / height:
            new_height = int(height * 0.9)
            new_width = int(image.width * new_height / image.height)
        else:
            new_width = int(width * 0.9)
            new_height = int(image.height * new_width / image.width)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=image.width, height=image.height, bg='black', highlightthickness=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk.PhotoImage(image))
    
    canvas.pack(expand=True, fill=tk.BOTH)

    root.after(delay_time, root.quit)
    root.mainloop()


if __name__ == '__main__':
    folder = 'C:/Users/ifzhao/Pictures/新建文件夹'
    delay = 5000  # delay in milliseconds

    images = [f for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.png')]
    while True:
        image_file = os.path.join(folder, random.choice(images))
        show_image(image_file, delay)
        time.sleep(1)


# 1. 导入必要的模块：`os` 用于读取文件夹里的文件名，`random` 用于随机选择图片，`time` 用于等待一段时间后继续执行程序，`PIL` 用于调整图片大小和显示图片。
# 2. 定义一个函数 `show_image()`，用于显示图片。首先创建一个全屏的窗口，然后打开图片，如果图片的大小大于屏幕大小，就按比例缩小图片，保证不变形。最后将图片显示到窗口中。
# 3. 在主程序中，先读取文件夹里的所有图片文件名，然后循环选择一张图片，显示一段时间后再显示下一张图片。用 `time.sleep()` 来等待间隔时间。
# 4. 运行代码，就可以随机播放指定文件夹里的图片啦！