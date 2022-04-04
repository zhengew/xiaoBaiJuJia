class User:
    Birth = 1980
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(f'我叫{self.name}, 今年{self.age}岁，{self.Birth}年出生.')

alex = User('alex', 42)

lis = [123, 456]