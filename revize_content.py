# 修改txt每行内容
import os

# 文件夹的路径
scr = 'E:\DATASET\Main'
# 获取文件夹下的txt的文件名
fs = os.listdir(scr)
print(fs)
for fz in fs:
    # txt文件路径
    src_folder = scr + "\\" + fz
    images = src_folder
    print(images)
    # 以只读模式读取文件

    # 路径
    path = images
    file = open(path, "r")
    lines = []
    for i in file:
        lines.append(i)  # 逐行将文本存入列表lines中

    file.close()

    # 创建一个新的列表，用于存储改变之后的内容
    new = []

    for line in lines:  # 逐行遍历

        # 选择需要添加的内容 line[0:] --->"E:\DATASET\VOC2028_hat\JPEGImages" + "\\" + line[0:]
        new.append("E:\DATASET\VOC2028_hat\JPEGImages" + "\\" + line[0:])

    file_write_obj = open(path, 'w')

    for var in new:
        file_write_obj.writelines(var)

    file_write_obj.close()