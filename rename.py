import os

# 图片类型字典
type_dict = {'png': '.png', 'jpg': '.jpg', 'bmp': '.bmp'}


def rename():
    path = "E:\\Project Warehouse\\Python Project\\BMS\\static\\media\\all_book\\" + input("输入文件夹名:")
    fileType = input("请输入文件类型:")
    # name = input("请输入开头名:")
    print("文件重命名中,更改类型为%s" % fileType)
    print(type_dict[fileType])
    count = 0
    filelist = os.listdir(path)
    for files in filelist:
        Olddir = os.path.join(path, files)
        if os.path.isdir(Olddir):
            continue
        Newdir = os.path.join(path, str(count) + type_dict[fileType])
        os.rename(Olddir, Newdir)
        count += 1
    print("一共修改了" + str(count) + "个文件")


list_img_name = []
list_read_img = []


def delete_end_str(path):
    count = 1
    for file in os.listdir(path):
        print(file)
        os.rename(os.path.join(path, file), os.path.join(path, str(count) + ".png"))
        count += 1


if __name__ == '__main__':

    path = "E:\\Project Warehouse\\Python Project\\BMS\\static\\media\\all_book\\" + input("输入文件夹名:")
    delete_end_str(path)
    # while True:
    #     rename()
    #     flag = input("输入Ture or False表示继续:")
    #     if flag == 'False':
    #         break
