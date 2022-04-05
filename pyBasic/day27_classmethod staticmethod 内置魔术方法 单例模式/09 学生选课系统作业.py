# https://www.cnblogs.com/Eva-J/articles/9235899.html

''' class
Student 学生类
Course 课程类
    # 周期 period
Admin 管理员类
'''
# 管理员登陆  admin 123
# 创建 学生（让用户输入学生信息，然后实例化，然后写到文件里）
#     课程 （让用户输入课程信息，然后实例化，然后写到文件里）
# 学生可以选多门课程 怎么存呢？
# 学生只要选课 - 文件修改(麻烦)

# 用上反射就简单
# 能不能  不管学生登陆 还是管理员登陆，这个地方不要用 if else   -- 进阶需求

# from 模块 import 一个类
import sys
# print(sys.modules[__name__])
# getattr(sys.modules[__name__], '名字') 反射本模块中的内容

