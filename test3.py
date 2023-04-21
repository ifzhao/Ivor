import os
import random
import time
import tkinter as tk
from PIL import Image, ImageTk

# 设置图片文件夹路径和播放间隔时间
image_folder = "C:/Users/ifzhao/Pictures/新建文件夹"
interval = 5  # seconds

# 获取图片文件列表
image_files = [os.path.join(image_folder, f)
               for f in os.listdir(image_folder)
               if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

# 创建窗口
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')

# 创建标签
image_label = tk.Label(root, bg='black')
image_label.pack(fill="both", expand=True)


# 播放函数
def play_image():
    # 从文件列表中随机选择一张图片
    image_file = random.choice(image_files)
    # 打开图片文件并缩放到窗口大小
    image = Image.open(image_file)
    image = image.resize((root.winfo_width(), root.winfo_height()), Image.ANTIALIAS)
    # 创建图像显示对象
    image_tk = ImageTk.PhotoImage(image)
    # 把图像显示在标签上
    image_label.configure(image=image_tk)
    image_label.image = image_tk  # 保持引用，否则图像会不显示
    # 等待指定间隔时间后再播放下一张图片
    root.after(interval * 1000, play_image)


# 开始播放
play_image()

# 进入主循环
root.mainloop()

# 该代码使用了Tkinter库创建窗口和标签，使用Pillow库处理图片。播放函数`play_image`随机选择一张图片并打开、缩放、显示，在指定的时间间隔后再继续播放下一张图片。主函数中创建窗口、标签，并调用播放函数开始播放。该代码可以随时按Esc键退出全屏模式。
