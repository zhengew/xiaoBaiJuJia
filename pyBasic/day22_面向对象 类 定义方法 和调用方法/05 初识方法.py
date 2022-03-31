''' 初识方法
'''
class Person: # 类名
    def __init__(self, name, sex, job, hp, weapon, ad): # 必须叫这个名字，不能改变的，所有的在一个具体的人物出现后拥有的属性，都可以写在这里
        self.name = name
        self.sex = sex
        self.job = job
        self.level = 0
        self.hp = hp
        self.weapon = weapon
        self.ad = ad

    def 搓(self, dog): # 方法,又有一个必须传的参数 --> self对象
        dog.blood -= self.ad
        print('%s给%s搓了澡,%s掉了%s点血, %s当前血量:%s' % (self.name, dog.name, dog.name, self.ad, dog.name,dog.blood))

class Dog:
    def __init__(self, name, blood, aggr, kind):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.kind = kind

    def 舔(self,person):
        if person.hp > self.aggr:
            person.hp -= self.aggr
        else:
            person.hp = 0
        print('%s舔了%s, %s掉了%s点血量, %s当前血量:%s' % (self.name, person.name, person.name, self.aggr,person.name, person.hp))

alex = Person('alex', '不详', '搓澡工', 260, '搓澡巾', 1) # 对象\实例 = 类名()   --> 实例化的过程
print('alex:', alex)
d1 = Dog('豆包', 1000, 100, 1)

alex.搓(d1)
d1.舔(alex)



