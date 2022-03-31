'''
# 面向对象的思想
# 类 对象实例 实例化
# 方法 实例变量

# class 语法 __init__方法
# self __dict__
'''

'''
# sys
    # sys.path
    # sys.argv 在执行python脚本的时候，写在python之后的所有内容，形成了一个列表
    # sys.modules 查看已经加载到内存中的所有模块
# os
    # 和文件 文件夹相关的
    # 和工作目录相关的
    # 和执行操作系统命令相关的
    # .path系列

# logging
    # 排错 数据分析 操作审计
    # 普通的输出(文件/屏幕)
    # 切分日志(时间/空间)

# shutil
    # 和文件相关的内容

'''

# 递归练习
    # 遍历文件夹下的所有文件 -- 掌握
    # 斐波那契额数列练习 -- 会写
    # 三级菜单 -- 看懂并知道实现方法
    # 查看文件夹的总大小 -- 看懂并知道实现方法
# 算法（用递归实现）
    # 二分查找 [1,2,3,4,5,6,7,8,9, 10, 27, 36m 46, 58, 69] - 有序列表
        # in index 从列表中找到一个值的位置
        # 实现上面的功能 -- 用代码实现 （今日作业）


# sys.argv 练习
    # 写一个脚本，在cmd里执行,完成文件的 复制，删除，重命名
    # python xxx.py  用户名 密码 cp 文件路径 目的地址
    # python xxx.py  用户名 密码 rm 文件路径 目的地址
    # python xxx.py  用户名 密码 rename 文件路径 目的地址

# 练习 使用walk来计算文件夹的总大小
# import os
# g = os.walk(os.path.dirname(os.path.dirname(__file__)))
# for i in g:
#     # print(i)
#     path, dir_lst, name_lst = i
#     print(path, name_lst)


# 整理笔记思路
    # 学习的梗概
        # 主要内容
    # 新的概念
    # 新的模块
    # 新的单词
    # 面试题/逻辑性比较强的题