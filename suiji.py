# 以下是使用Python的Pygame库实现随机播放指定文件夹里的图片，并且可以控制播放间隔的代码：


import os
import random
import time
import pygame

# 设置窗口大小为图片的分辨率
pygame.init()
pygame.display.set_caption("Random Image Player")

# 定义图片文件夹路径和播放间隔时间（秒）
image_folder = "C:/Users/ifzhao/Pictures/新建文件夹"
play_interval = 2

# 获取图片列表
image_list = []
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_list.append(os.path.join(image_folder, filename))

# 随机播放图片
while True:
    # 随机选择一张图片
    image_path = random.choice(image_list)

    # 加载图片并设置窗口大小和位置
    image = pygame.image.load(image_path)
    width, height = image.get_size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(os.path.basename(image_path))
    pygame.display.set_icon(image)

    # 显示图片
    screen.blit(image, (0, 0))
    pygame.display.flip()

    # 等待播放间隔时间
    time.sleep(play_interval)

    # 处理窗口关闭事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# 在上面的代码中，你需要修改以下部分以适应自己的需求：
#
# - `image_folder`：将其修改为包含要播放的图片的文件夹路径。
# - `play_interval`：将其修改为两张图片之间的播放间隔时间（秒）。
# - `screen`：如有必要，可以设置窗口的大小和位置。
#
# 运行代码后，你将看到一张随机选择的图片，该窗口将在每个播放间隔时间（秒）后更新以显示下一张随机选择的图片。在窗口上单击“关闭”按钮将停止播放并退出程序。