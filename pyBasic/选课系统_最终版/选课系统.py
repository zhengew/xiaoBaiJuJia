import sys
import pickle
import os

# 用户信息： 用户名|密码|ident(Student/Manager)
USERINFO = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/userinfo'
STUINFO = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/stuinfo'
COURSE = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/选课系统_最终版/db/course'
login_user = ''
class Course(object):
    def __init__(self,name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Student(object):

    opt_lst = [('查看课程', 'show_courses'),('选择课程','choose_course'),
                   ('查看已选课程', 'show_selected'), ('退出', 'exit')]

    def __init__(self, name):
        self.name = name
        self.cname = [] # 存储课程

    def show_courses(self):
        with open(COURSE, mode='rb') as f:
            index = 1
            while True:
                try:
                    course = pickle.load(f)
                    print('%d:\t%s\t%s\t%s\t%s'%(index, course.name, course.price, course.period, course.teacher))
                    index += 1
                except EOFError:
                    break

    def choose_course(self):
        self.show_courses()
        opt = input('请选择课程名称: ').strip()
        with open(STUINFO, mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    w = open('temp', mode='ab')
                    if obj.name == login_user:
                        if opt in obj.cname:
                            if os.path.exists('temp'): os.remove('temp')
                            return '%s已选择课程:%s'% (obj.name, opt)
                        else:
                            obj.cname.append(opt)
                            pickle.dump(obj,w)
                    else:
                        pickle.dump(obj,w)
                except EOFError:
                    break
        os.remove(STUINFO)
        os.rename('temp', STUINFO)
        return '选择课程成功'

    def show_selected(self):
        with open(STUINFO, mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.name == login_user:
                        print('%s : %s' % (obj.name, str(obj.cname)))
                except EOFError:
                    break

    def exit(self):
        sys.exit()




class Manager(object):

    opt_lst = [('创建课程','create_course'),('创建学生','create_student'),
                   ('查看课程','show_courses'),('查看学生','show_students'),
                   ('查看学生和已选课程','show_stu_course'),('退出','exit')]

    def __init__(self, name):
        self.name = name

    def create_course(self):
        cname = input('课程名称:').strip()
        flag = ''
        if os.path.exists(COURSE) and os.path.isfile(COURSE):
            course_lst = []
            with open(COURSE, mode='rb') as f:
                while True:
                    try:
                       course = pickle.load(f)
                       course_lst.append(course.name)
                    except EOFError:
                        break
                if cname in course_lst:
                    return '%s 课程已存在' % cname
                else:
                    with open(COURSE, mode='ab') as f:
                        price = input('价格:').strip()
                        period = input('课程周期:').strip()
                        teacher = input('授课老师:').strip()
                        obj = Course(cname, price, period, teacher)
                        pickle.dump(obj, f)
                    flag = '%s 课程创建成功' % cname
        else:
            price = input('价格:').strip()
            period = input('课程周期:').strip()
            teacher = input('授课老师:').strip()
            with open(COURSE, mode='ab') as f:
                obj = Course(cname, price, period, teacher)
                pickle.dump(obj, f)
            flag = '%s 课程创建成功' % cname
        return flag

    def create_student(self):
        name = input('用户名:').strip()
        pwd = input('密码:').strip()
        # 先判断用户是否为已注册用户
        if os.path.exists(STUINFO):
            with open(STUINFO, mode='rb') as f:
                while True:
                    try:
                        stu = pickle.load(f)
                        if name == stu.name:
                            return '用户已存在'
                    except EOFError:
                        break
        else:
            with open(USERINFO, mode='r',encoding='utf-8') as f:
                for info in f:
                    uname, upwd, ident = info.strip().split('|')
                    if name == uname:
                        return '用户已存在'
                f.close()
        # 新用户写入用户文件
        with open(USERINFO, mode='a',encoding='utf-8') as f:
            f.seek(0, 2)
            f.write('%s|%s|Student\n'%(name, pwd))
            f.flush()
        # 将学生对象写入 STUINFO
        obj = Student(name)
        with open(STUINFO, mode='ab') as f:
            pickle.dump(obj, f)
        return '创建成功'

    def show_courses(self):
        with open(COURSE, mode='rb') as f:
            index = 1
            while True:
                try:
                    course = pickle.load(f)
                    print('%d:\t%s\t%s\t%s\t%s'%(index, course.name, course.price, course.period, course.teacher))
                    index += 1
                except EOFError:
                    break

    def show_students(self):
        with open(STUINFO, mode='rb') as f:
            index = 1
            while True:
                try:
                    stu = pickle.load(f)
                    print('%d:\t%s' % (index, stu.name))
                    index += 1
                except EOFError:
                    break

    def show_stu_course(self):
        with open(STUINFO, mode='rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    print('%s : %s' % (obj.name, str(obj.cname)))
                except EOFError:
                    break

    def exit(self):
        sys.exit()


def login():
    '''
    :return: uname,ident(Student/Manager)
    '''
    name = input('用户名:').strip()
    pwd = input('密码:').strip()
    with open(USERINFO, mode='r', encoding='utf-8') as f:
            for info in f:
                uname, upwd, ident = info.strip().split('|')
                if name == uname and pwd == upwd:
                    return uname, ident
            else:
                return False

def main():
    ret = login()
    if ret:
        while True:
            sys.modules[__name__].login_user = ret[0]
            cls = getattr(sys.modules[__name__], ret[1])
            for index, opt in enumerate(cls.opt_lst,1):
                print(index, opt[0])
            obj = cls(ret[0])
            opt = int(input('请选择:').strip())
            if hasattr(obj, cls.opt_lst[opt-1][1]):
                res = getattr(obj,  cls.opt_lst[opt-1][1])()
                if res != None:
                    print(res)
    else:
        print('用户名或密码错误')

if __name__ == '__main__':
    main()












# 创建学生
    # 让用户输入用户名 密码
    # 实例化一个对象
    # 把用户名 密码 写到userinfo
    # 把学生对象写到stuinfo文件里
