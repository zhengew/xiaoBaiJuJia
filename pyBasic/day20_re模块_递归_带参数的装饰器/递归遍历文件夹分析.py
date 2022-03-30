# 2. os 模块，查看一个文件夹下的所有文件，这个文件夹下面还有文件夹，不知道文件又多少层,不能用walk
import os
import sys


def func(path):
    lis = os.listdir(path)
    for file in lis:
        if os.path.isdir(os.path.join(path, file)):
            func(os.path.join(path, file))
        elif os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files


def main():
    path = os.path.join(os.path.dirname(__file__), 'dira')
    print(os.listdir(os.path.join(path, 'dirb', 'dirc')))
    global files
    files = []
    file = func(path)
    print(file)
if __name__ == '__main__':
    main()

