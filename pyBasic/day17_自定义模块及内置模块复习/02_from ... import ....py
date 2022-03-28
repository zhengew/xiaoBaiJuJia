# # 1 打印当前名称空间中的所有命名
# print(globals())
'''
from ... import...
1.方便直接用
2.容易根据上下文覆盖同名成员
'''

'''
py文件当作脚本使用, __name__  == __main__
py文件当作模块被别人引用，__name__ == 模块名

模块需要被调试时，加上:
if '__name__' == '__main__':
    '调试代码'
'''

'''
模块的搜索路径: 内存中已加载的模块 -> 内置模块 -> sys.path
sys.modules() -> 查看系统内置模块
sys.path() -> 系统路径

sys.path() 会自动将当前文件所在的目录添加到 sys.path列表中；

如果你想要引用你自定义的模块：
要么你就将这个模块放到当前目录下面，要么就手动添加到sys.path中
'''
import sys
print(sys.modules)
print(sys.path)