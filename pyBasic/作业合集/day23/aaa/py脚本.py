'''
# sys.argv 练习
    # 写一个脚本，在cmd里执行,完成文件的 复制，删除，重命名
    # python xxx.py  用户名 密码 cp 文件路径 目的地址
    # python xxx.py  用户名 密码 rm 文件路径
    # python xxx.py  用户名 密码 rename 文件路径
    # 待完成
    # python xxx.py  用户名 密码 move 文件路径 目的地址
    # python xxx.py  用户名 密码 mkdir 文件路径 目的地址
    # 在这个基础上实现 move 移动，把一个文件或者文件夹移动到另一个位置
'''
import os
import sys
import shutil

class PyScript:
    ''' py脚本，实现对文件的复制，删除，重命名，移动文件，新建文件夹'''
    # 拷贝
    def copy(self, srcfile, topath):
        shutil.copy2(srcfile, topath)

     # 删除
    def remove(self, path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)

    # 重命名
    def rename(self, path, newname):
        if os.path.exists(path):
            os.rename(path, newname)

    # 移动文件
    def move(self, frompath, topath):
        shutil.move(frompath, topath, copy_function=shutil.copy2())

    # 新建文件夹
    def mkdir(self, path):
        os.mkdir(path)

def main():
    print(sys.argv)  # ['/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/作业合集/day23/py脚本.py']
    str = 'xxx.py  用户名 密码 cp 文件路径 目的地址'
    # str = /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/作业合集/day23/py脚本.py
    script = PyScript()
    argv = sys.argv
    if len(argv) > 5:
        if argv[3].lower() == 'cp' and len(argv) == 6:
            if os.path.exists(argv[4]) and os.path.exists(argv[5]):
                script.copy(argv[4], os.path.join(argv[5], os.path.basename(argv[4])))

    else:
        print('您输入的命令无效!')

if __name__ == '__main__':
    main()