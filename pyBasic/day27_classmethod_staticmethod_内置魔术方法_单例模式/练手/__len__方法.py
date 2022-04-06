# len(对象) 需要在类中实现 __len__ 方法
class Clas:
    def __init__(self, name):
        self.name = name
        self.students = []
    def append(self):
        self.students.append(self.name)
    def __len__(self): # 通过实现 __len__ 方法，返回给对象 self.students的长度
        return len(self.students)

    def len(self):
        return len(self.students)

py22 = Clas('py22期')
py22.students.append('alex')
py22.students.append('wusir')

print(py22.students)
print(len(py22.students))
# TypeError: object of type 'Clas' has no len()
print(len(py22))  # 如果 类中未实现 __len__方法，会抛出TypeError异常