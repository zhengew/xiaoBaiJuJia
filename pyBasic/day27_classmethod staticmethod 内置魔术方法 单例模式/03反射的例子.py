# 文件操作
class File:
    # 因为每次实例化对象时都要用到这个列表，所以把它设置成静态变量，所有的实例化对象都共用一份
    lst = [('读文件', 'read'), ('写文件', 'write'), ('删除文件', 'remove'),
           ('文件重命名', 'rename'), ('复制文件', 'copy'), ('移动文件', 'move')]
    def __init__(self, filepath):
        self.filepath = filepath
    def write(self):
        print('in write func')
    def read(self):
        print('in read func')
    def remove(self):
        print('in remove func')
    def rename(self):
        print('in rename func')
    def copy(self):
        print('in copy func')
    def move(self):
        print('in move func')

f = File('') # 实例化 File
while True:
    for index, opt in enumerate(File.lst, 1):
        print(index, opt[0])

    num = int(input('请输入您要做的操作序号>>>'))
    if hasattr(f, File.lst[num-1][1]):
        getattr(f, File.lst[num-1][1])()


# 显示所有可以做的操作
# 1. 读文件
# 2. 写文件
# 3. 删除文件
# 4. 文件重命名
# 5. 复制文件

# 作业：用发射实现
# python xx.py cp path1 path2
# python xx.py rm path
# python xx.py mv path1 path2