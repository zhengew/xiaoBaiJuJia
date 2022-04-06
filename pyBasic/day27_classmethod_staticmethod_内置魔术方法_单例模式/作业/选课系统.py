'''
选课系统
# 课程
    # 属性：课程名、价格、周期、老师
# 学生
    # 属性: 姓名 所选课程
    # 方法：查看可选课程、选择课程、查看已选课程、退出程序
# 管理员
    # 属性：姓名
    # 方法：建课程、创建学生学生账号、查看所有课程、查看所有学生、查看所有学生的选课情况、退出程序

db文件：
    course.cname = students.cname
    students.sname = smteller.name

    course
        cname(pk), price, period, teacher
    students
        sname(pk), cname (已选课程)
    smteller
        name(pk), pwd, limits (1.学生， 2.管理员)
'''
import time
import os
import sys
import pickle

class Course(object):
    '''
    课程类  课程名，价格，周期，授课老师
    '''
    def __init__(self, cname, price, period, teacher):
        self.cname = cname
        self.price = price
        self.period = period
        self.teacher = teacher

class Student(object):
    def __init__(self, sname, cname):
        self.sname = sname

class Admin(object):
    '''
    管理员
        默认账户 admin 密码 123456
        首次登陆需重置密码
    '''
    def __init__(self, name):
        self.name = name
login_user = {'name':None, 'limits':'1'}
def login():
    path = os.path.join(os.path.dirname(__file__), 'db', 'smteler')
    login_name = input('用户名: ').strip()
    login_pwd = input('密码: ').strip()
    with open(path, 'r', encoding='utf-8') as f:
        for info in f:
            name, pwd, limits = info.strip().split('|')
            if login_name == name and login_pwd == pwd:
                # 如果登陆成功，返回 (用户名和权限)
                # limits:1-学生, 2-管理员
                login_user['name'] = name
                login_user['limits'] = limits
                return True
        else:
            return False

def quit():
    return 0

class Mypickle:
    def __init__(self, path):
        self.path = path
    def dump(self, obj):
        with open(self.path, mode='ab') as f:
            pickle.dump(obj, f)

    def load(self):
        with open(self.path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
# 课程文件
course_path = sys.path.join(sys.path.dirname(__file__), 'db', 'course')

class Admin_opt(object):
    func_lst = [('创建课程', 'create_courses'), ('创建账号', 'create_account'),
                ('查看所有课程', 'show_courses'), ('查看所有学生', 'show_students'),
                ('查看所有学生选课情况', 'show_stu_course'), ('退出系统', 'quit'),
                ]

    def create_courses(self):

        try:
            cname = input('课程名: ').strip()
            price = input('价格: ').strip()
            period = input('周期: ').strip()
            teacher = input('授课老师: ').strip()
            course = Course(cname, price, period, teacher)
            with open(course_path,mode='ab') as f:
                Mypickle(course_path).dump(course)
        except:
            return '输入数据异常'


class Student_opt(object):
    func_lst = [('查看已选课程', 'show_selected_course'), ('查看所有课程', 'show_courses'),
                ('选择课程', 'selected_courses'),('退出系统', 'quit')
                ]

def run():
    flag = True
    while flag:
        if login():
            obj = None # 此处保存实例化的名字
            if login_user['limits'] == '2':
                obj = Admin_opt()
                for index, opt in enumerate(Admin_opt.func_lst, 1):
                    print(f'{index} : {opt[0]}')
            elif login_user['limits'] == '1':
                obj = Student_opt()
                for index, opt in enumerate(Student_opt.func_lst, 1):
                    print(f'{index} : {opt[0]}')

            opt = input('尊敬的%s,欢迎登陆选课系统，请选择>>>'% login_user['name'])
            if hasattr(obj, Admin_opt.func_lst[int(opt) - 1][1]):
                getattr(obj, Admin_opt.func_lst[int(opt) - 1][1])()
        else:
            opt = input('用户名或密码错误,是否继续？按q退出>>>')
            if opt.upper() == 'Q':
                flag = quit()

def main():
    # run()
    course_path = sys.path.join(sys.path.dirname(__file__), r'db/course')
    print(course_path)
if __name__ == '__main__':
    main()