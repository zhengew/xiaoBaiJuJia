STUINFO = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/tmp'
import pickle

class Student(object):

    opt_lst = [('查看课程', 'show_courses'),('选择课程','choose_course'),
                   ('查看已选课程', 'show_selected'), ('退出', 'exit')]

    def __init__(self, name):
        self.name = name
        self.cname = [] # 存储课程

# with open(STUINFO, mode='rb') as f:
#     while True:
#         try:
#             stu =  pickle.load(f)
#             print(stu.__dict__)
#         except EOFError:
#             break



s1 = Student('alex')
s2 = Student('tbjx')
print(s1.__dict__)
# s1.cname.append('python')
# s2.cname.append('java')

import pickle
with open('tem',mode='ab') as f:
    pickle.dump(s1, f)
    pickle.dump(s2, f)

print(s1.__dict__)
print(s2.__dict__)
print('*'*100)
print()
# with open('tem', mode='rb') as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             print(obj.__dict__)
#         except EOFError:
#             break

# with open('tem', mode='rb') as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             print(obj.__dict__)
#             w = open('temp', mode='wb')
#             if obj.name == 'tbjx':
#                 obj.cname.append('java')
#                 obj.cname.append('python')
#             pickle.dump(obj,w)
#         except EOFError:
#             break
#
# import os
# os.remove(r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/tem')
# os.rename(r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/temp', r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/tem')
#
#
#
with open(r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/stuinfo', mode='rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            print(obj.__dict__)
        except EOFError:
            break


# s1.cname.append('java')
# print(s1.__dict__)
# print(s2.__dict__)