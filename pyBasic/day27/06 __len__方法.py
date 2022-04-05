'''
__len__
'''
class Cls:
    def __init__(self, name):
        self.name = name
        self.students = []
    def len(self):
        return len(self.students)
    def __len__(self): # 重写len()函数中的__len__方法，就可以使用len()
        return len(self.students)
py22 = Cls('py22')
py22.students.append('alex')
py22.students.append('tbjx')
py22.students.append('大壮')

print(len(py22)) # 因为len函数在内部就是调用了__len__(), 重新len函数中的__len__方法
print(py22.__len__()) # 等价与 对象在调用自己类中的__len__,其实就是鸭子类型
print(py22.len())


class Pow:
    def __init__(self, n):
        self.n = n
    def __pow2__(self):
        return self.n ** 2

def pow2(obj):
    return obj.__pow2__()

obj = Pow(10)
print(pow2(obj))