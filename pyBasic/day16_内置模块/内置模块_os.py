''' 内置模块 os
os : 和操作系统相关的操作封装到这个模块中
'''
import os

'''
1. 和文件操作相关， 重命名，删除等
'''
# 1> 删除
# os.remove(r"a.txt") # 如果是绝对路径 路径前加 r

# 2> 重命名
# os.rename('c.txt', 'b.txt')

# 3> 删除目录，必须是空目录
# os.removedirs("aa") # OSError: [Errno 66] Directory not empty: 'aa'

# 4> 使用 shutil 模块，可以删除带内容的目录 sh - > shell util
# import shutil
# shutil.rmtree("aa")

'''
2.可路径相关的操作，被封装到另一个子模块中: os.path
'''
# 1> dirname() 获取当前文件所在的父目录，不判断路径是否存在
res = os.path.dirname(r"/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/bin/a.txt")
print(res) # /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/bin

# 2> basename() 获取文件名
res = os.path.basename(r"/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/bin/a.txt")
print(res) # a.txt

# 3> split() 把路径中路径名和文件名切分开，结果是元组类型
res = os.path.split(r"/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/bin/a.txt")
print(res) # ('/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/bin', 'a.txt')

# 4> join() 拼接路径
path = os.path.join("/user", "erwei.zheng", "PycharmProjects")
print(path)

# 5> abspath() 获取绝对路径,
# a> 如果是/开头的路径，默认是当前盘符下
res = os.path.abspath("/Users/erwei.zheng/")
print(res) # /Users/erwei.zheng
# b> 如果不是/开头,默认当前路径
res = os.path.abspath("erwei.zheng")
print(res) # /Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day16_内置模块/erwei.zheng

# 6> 判断是不是？
# a> isabs() 是否绝对路径
res = os.path.isabs(r"/user/erwei.zheng/PycharmProjects")
print(res) # True
res = os.path.isabs("a.txt")
print(res) # False

# b> isdir() 是否文件夹？ 如果文件不存在 False, 如果存在去路径下判断 是否
print(os.path.isdir(r"/Users/erwei.zheng")) # True
print(os.path.isabs("a.txt")) # False

# c> exists() 是否存在
print(os.path.exists("a.txt"))

# d> isfile() 是否文件？文件不存在 False
print(os.path.isfile("a.txt"))

# e> islink() 是否快捷键

# os.listdir() 将当前目录下的文件或文件夹保存到列表
print(os.listdir(os.path.dirname(__file__)))