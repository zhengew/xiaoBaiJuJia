import sys
import pickle
USERINFO = r'D:\python_22\选课系统\userinfo'
STUINFO = r'D:\python_22\选课系统\stuinfo'


class Course(object):

    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

class Student(object):
    opt_lst = [('查看课程', 'show_courses'),('选择课程','choose_course'),
               ('查看已选课程', 'show_selected'), ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_courses(self):
        pass
    def choose_course(self):
        pass
    def show_selected(self):
        pass
    def exit(self):
        pass

class Manager(object):
    opt_lst = [('创建课程','create_course'),('创建学生','create_student'),
               ('查看课程','show_courses'),('查看学生','show_students'),
               ('查看学生和已选课程','show_stu_course'),('退出','exit')]
    def __init__(self,name):
        self.name = name
    def create_course(self):
        pass
    def create_student(self):
        usr = input('username :')
        stu = Student(usr)
        with open(USERINFO,mode = 'a',encoding='utf-8') as f:
            f.write('%s|123456|Student\n'%(usr))
        with open(STUINFO,mode = 'ab') as f:
            pickle.dump(stu,f)
        print('%s学生创建成功'%stu.name)

    def show_courses(self):
        pass
    def show_students(self):
        pass
    def show_stu_course(self):
        pass
    def exit(self):
        pass

# 用户 输入用户名 密码 判断用户是否合法和身份是啥?
def login():
    '''

    :return: 登录成功:用户名,身份
              登录失败:False
    '''
    username = input('username :')
    password = input('password :')
    with open(USERINFO,encoding='utf-8') as f:
        for line in f:
            usr,pwd,ident = line.strip().split('|')
            if usr == username and password == pwd:
                return usr,ident
        else:
            return False

ret = login()
if ret:
    print('登录成功,%s,欢迎使用选课系统'%ret[0])
    cls = getattr(sys.modules[__name__],ret[1])
    print(cls,Manager,Student)
    if ret[1] == 'Manager':
        obj = Manager(ret[0])
    elif ret[1] == 'Student':
        with open(STUINFO,'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    if obj.name == ret[0]:
                        break
                except EOFError:print('没有这个学生,出现了不可思议的错误!')
    for index,opt in enumerate(cls.opt_lst,1):
        print(index,opt[0])
    num = int(input('您要选择的操作 :').strip())
    if hasattr(obj,cls.opt_lst[num-1][1]):
        getattr(obj,cls.opt_lst[num-1][1])()
else:
    print('登录失败')


# 创建学生
    # 让用户输入用户名 密码
    # 实例化一个对象
    # 把用户名 密码 写到userinfo
    # 把学生对象写到stuinfo文件里
