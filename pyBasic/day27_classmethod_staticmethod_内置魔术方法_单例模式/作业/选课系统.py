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
    course.cname = studentInfos.cname
    students.sname = smteller.name

    course
        cname(pk), price, period, teacher
    studentInfos
        sname(pk), cname (已选课程)
    smteller
        sname(pk), pwd, limits (1.学生， 2.管理员)
'''

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
    def __init__(self, sname):
        self.sname = sname
        self.cnames = []
    def append_cname(self,course):
        self.cnames.append(course)

class Teller(object):
    '''
    管理员
        默认账户 admin 密码 123456
        首次登陆需重置密码
    '''
    def __init__(self, sname, pwd, limits):
        self.sname = sname
        self.pwd = pwd
        self.limits = limits

# 当前登陆账户权限
login_user = {'name':None, 'limits':'1'}
# 课程文件
course_path = os.path.join(os.path.dirname(__file__), 'db', 'course')
# 账户文件
teller_path = os.path.join(os.path.dirname(__file__), 'db', 'smteler')
# 学生选课信息
studentInfos_path = os.path.join(os.path.dirname(__file__), 'db', 'studentInfos')
def login():
    # path = os.path.join(os.path.dirname(__file__), 'db', 'admin')
    login_name = input('用户名: ').strip()
    login_pwd = input('密码: ').strip()
    for info in Mypickle(teller_path).load():
        print(info.__dict__)
        if login_name == info.sname and login_pwd == info.pwd:
            # 如果登陆成功，返回 (用户名和权限)
            # limits:1-学生, 2-管理员
            login_user['name'] = info.sname
            login_user['limits'] = info.limits
            return True
    else:
        return False

class Mypickle:
    def __init__(self, path):
        self.path = path
    def dump(self, obj):
        with open(self.path, mode='ab') as f:
            pickle.dump(obj, f)
            f.flush()
            f.close()

    def load(self):
        with open(self.path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

class Sys_func(object):
    func_dic = {'2':[('创建课程', 'create_courses'), ('创建账号', 'create_account'),
                ('查看所有课程', 'show_courses'), ('查看所有学生', 'show_students'),
                ('查看所有学生选课情况', 'show_stu_course'), ('退出系统', 'quit'),
                ],\
                '1':[('查看已选课程', 'show_selected_course'), ('查看所有课程', 'show_courses'),
                ('选择课程', 'selected_courses'),('退出系统', 'quit')
                ]}
    # 创建课程
    def create_courses(self):
        cname = input('课程名: ').strip()
        price = input('价格: ').strip()
        period = input('周期: ').strip()
        teacher = input('授课老师: ').strip()
        f = Mypickle(course_path)
        if os.path.exists(course_path):
            if os.path.isfile(course_path):
                for course in f.load():
                    if cname == course.cname:
                        print(f'{course.cname} 课程已存在， 请添加其他课程')
                        print(course.__dict__)
                        break
                else:
                    course = Course(cname, price, period, teacher)
                    f.dump(course)
                    print('创建课程了...')

        else:
            course = Course(cname, price, period, teacher)
            f.dump(course)

    # 创建学生
    def create_account(self):
        '''
        smteller
        name(pk), pwd, limits (1.学生， 2.管理员)
        :return:
        '''
        sname = input('账号: ').strip()
        pwd = input('密码: ').strip()
        limits = input('用户权限 1-学生, 2-管理员: ').strip()

        f = Mypickle(teller_path)
        if os.path.exists(teller_path):
            if os.path.isfile(teller_path):
                for teller in f.load():
                    if sname == teller.sname:
                        print(f'{teller.sname} 账号已存在， 请添加其他账号')
                        print(teller.__dict__)
                        break
                else:
                    teller = Teller(sname, pwd, limits)
                    f.dump(teller)
                    print('创建学生账号了...')

        else:
            teller = Teller(sname, pwd, limits)
            f.dump(teller)

    # 查看所有课程'， 'show_courses'
    def show_courses(self):
        print(f'课程名称\t\t价格\t\t周期\t\t授课老师')
        for i in Mypickle(course_path).load():
            print('%13s%15s%15s%8s' %(i.cname, i.price, i.period, i.teacher))

    # '查看所有学生', 'show_students'
    def show_students(self):
        print(f'账号\t\t密码\t\t权限')
        for i in Mypickle(teller_path).load():
            if i.limits == '1':
                print('%-5s%13s%8s' %(i.sname, i.pwd, i.limits))
    # '退出系统', 'quit'
    def quit(self):
        sys.exit()

    # '选择课程', 'selected_courses'
    def selected_courses(self):
        '''
        studentInfos
        sname(pk), cname (已选课程)
        :return:
        '''

        self.show_courses()
        opt = input('请选择课程>>>').strip()
        f = Mypickle(studentInfos_path)
        stu = Student(login_user['name'])
        if os.path.exists(studentInfos_path):
            if os.path.isfile(studentInfos_path):
                for course in f.load():
                    if opt in course.cnames:
                        print(f'{login_user["name"]}已选择课程: {opt}')
                        print(course.__dict__)
                        break
                else:
                    stu.append_cname(opt)
                    f.dump(stu)
                    print('选课信息已写入studentInfos...')

        else:
            stu.append_cname(opt)
            f.dump(stu)

    # '查看已选课程', 'show_selected_course'
    def show_selected_course(self):
        stu_course = set()
        for info in Mypickle(studentInfos_path).load():
            if info.sname == login_user['name']:
                stu_course.add(info.cnames[0])
        print(stu_course)

    # '查看所有学生选课情况', 'show_stu_course'
    def show_stu_course(self):
        stu_course = []
        for info in Mypickle(studentInfos_path).load():
            stu_course.append((info.sname, info.cnames[0]))

        infos = {}
        for i in range(len(stu_course)):
            name, value = stu_course[i]
            infos.setdefault(name, set())

        for key, value in stu_course:
            infos[key].add(value)

        for k, v in infos.items():
            print(k, v)


def run():
    flag = True
    if login():
        obj = Sys_func() # 此处保存实例化的名字
        for index, opt in enumerate(Sys_func.func_dic[login_user['limits']], 1):
            print(f'{index} : {opt[0]}')
        opt = input('尊敬的%s,欢迎登陆选课系统，请选择>>>' % login_user['name'])
        while flag:
            # print(opt, type(opt))
            if hasattr(obj, Sys_func.func_dic[login_user['limits']][int(opt) - 1][1]):
                getattr(obj, Sys_func.func_dic[login_user['limits']][int(opt) - 1][1])()
            if input('操作成功，是否选择其他功能？ 1-继续操作，2-退出系统>>>').strip() == '2':
                flag = False
            else:
                for index, opt in enumerate(Sys_func.func_dic[login_user['limits']], 1):
                    print(f'{index} : {opt[0]}')
                opt = input('请选择>>>')
    else:
        print('用户名或密码错误')

def main():
    run()

if __name__ == '__main__':
    main()