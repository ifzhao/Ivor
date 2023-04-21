import os
from random import choice
from PIL import Image
import time
import tkinter as tk

# 指定图片文件夹路径
folder_path = "C:/Users/ifzhao/Pictures/新建文件夹"

# 播放间隔（秒）
play_interval = 5

# 获取文件夹下所有图片文件名并保存到列表中
image_list = []
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_list.append(os.path.join(folder_path, filename))

# tkinter 窗口配置
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(screen_width, screen_height))
root.configure(background='black')
root.attributes('-fullscreen', True)

# 创建图片显示区域
image_area = tk.Label(root)
image_area.pack(fill=tk.BOTH, expand=True)


# 播放图片函数
def play_image():
    # 从图片列表中随机选择一张图片
    image_path = choice(image_list)
    # 打开图片并调整大小
    image = Image.open(image_path)
    image_width, image_height = image.size
    if image_width > screen_width or image_height > screen_height:
        if image_width > image_height:
            new_width = screen_width
            new_height = int(image_height * screen_width / image_width)
        else:
            new_height = screen_height
            new_width = int(image_width * screen_height / image_height)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
    # 在 Label 中显示图片
    image_tk = ImageTk.PhotoImage(image)
    image_area.configure(image=image_tk)
    image_area.image = image_tk
    # 播放下一张图片
    root.after(play_interval * 1000, play_image)


# 开始播放第一张图片
play_image()

# 运行 tkinter 主循环
root.mainloop()
# ```
#
# 该代码使用了 Python 的 `os`、`random`、`PIL` 和 `tkinter` 模块。其中，`os` 模块用于获取指定文件夹下的所有图片文件名，`random` 模块用于随机选择一张图片，`PIL` 模块用于打开和调整图片大小，`tkinter` 模块用于创建图形用户界面和显示图片。具体做法如下：
#
# 1. 首先定义图片文件夹路径和播放间隔。
#
# 2. 使用 `os` 模块获取指定文件夹下所有后缀为 `.jpg` 或 `.png` 的文件名，并保存到一个列表中。
#
# 3. 使用 `tkinter` 模块创建一个全屏窗口，并将窗口背景设为黑色。然后创建一个 `Label` 控件用于显示图片，并将其填充整个窗口。
#
# 4. 定义一个播放图片的函数 `play_image()`。该函数会从图片列表中随机选择一张图片，并使用 `PIL` 模块打开并调整其大小，以保证图片不变形且大小合适屏幕显示。最后将调整后的图片显示在 `Label` 中，并使用 `tkinter` 的 `after()` 方法设定下一次播放时间。
#
# 5. 调用 `play_image()` 函数
