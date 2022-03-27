''' 内置模块 sys
sys : 和python解释器相关的操作.
'''

import sys
'''
1. 获取命令行方式运行的脚本后面的参数，仅仅在脚本方式运行时，获取脚本的参数值
'''
# print(sys.argv[0]) # 0 脚本名
# print(sys.argv[1]) # 1 脚本的第一个参数

'''
2. sys.path 解释器获取模块的路径
'''

'''
3. sys.modules 获取当前已经加载到内存中的模块
'''
print(sys.modules, type(sys.modules))