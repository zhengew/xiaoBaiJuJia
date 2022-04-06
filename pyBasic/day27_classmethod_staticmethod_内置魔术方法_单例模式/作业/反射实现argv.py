# 作业：用反射实现
# python xx.py cp path1 path2
# python xx.py rm path
# python xx.py mv path1 path2
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
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)

    # 移动文件
    def move(self, frompath, topath):
        if os.path.exists(frompath) and os.path.exists(topath):
            shutil.move(frompath, topath, copy_function=shutil.copy2)

def main():
    print(sys.argv)  # ['/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/作业合集/day23/py脚本.py']
    str = 'xxx.py  用户名 密码 cp 文件路径 目的地址'
    # str = /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/作业合集/day23/py脚本.py
    script = PyScript()
    argv = sys.argv
    if len(argv) >= 5:
        if argv[1] == 'test1' and argv[2] == '123': # login() 函数
            if argv[3].lower() == 'cp' and len(argv) == 6:
                if os.path.exists(argv[4]) and os.path.exists(argv[5]):
                    script.copy(argv[4], os.path.join(argv[5], os.path.basename(argv[4])))
            elif argv[3].lower() == 'rm' and len(argv) == 5:
                # python xxx.py  用户名 密码 rm 文件路径
                script.remove(argv[4])
            elif argv[3].lower() == 'mv' and len(argv) == 6:
                # python xxx.py  用户名 密码 move 文件路径 目的地址
                script.move(argv[4], argv[5])
        else:
            print('用户名或密码错误')

    else:
        print('您输入的命令无效!')
    # a = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/作业合集/day23/aaa'
    # b = 'ddd'
    # script.mkdir(os.path.join(a, b))

def main():
    print(sys.argv)
    getattr(sys.modules[__name__].PyScript, 'copy')()
if __name__ == '__main__':
    main()