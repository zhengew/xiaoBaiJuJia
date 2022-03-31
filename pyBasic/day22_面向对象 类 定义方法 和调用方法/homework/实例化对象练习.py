''' 实例化对象练习
student类
属性：
name
sex
age
grade
'''
class Student():
    def __init__(self, name, age, grade, sex = "M"):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex


lucu = Student('lucy', 15, 1, '女')


print(lucu.__dict__)
lucu.name = 'zew'
print(lucu.name)
lucu.money = 10000
print(lucu.__dict__)
del lucu.money
print(lucu.__dict__)