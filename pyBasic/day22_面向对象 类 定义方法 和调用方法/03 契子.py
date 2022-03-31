# 游戏公司
    # 人狗大战
# 人:
    # 名字 性别 职业 等级 血条 武器 攻击力
    # 技能: 搓澡
# 狗:
    # 名字 品种 血条
    # 技能

# alex = {
#     'name':'alex',
#     'sex':'不详',
#     'job':'搓澡工',
#     'level':0,
#     'hp':250,
#     'weapon':'搓澡巾',
#     'ad':1
# }

# 小白 = {
#     'name':'小白',
#     'kind':'泰迪',
#     'hp':5000,
#     'ad':249,
# }

# 1.你怎么保证所有的玩家初始化的时候都拥有相同的属性？
# 2.每来一个新的玩家，我们都自己手动的创建一个字典，然后向字典中填值？
# 3.人和狗的技能如何去写？

def Person(name, sex, job, hp, weapon, ad, level=0):    # 人模子
    def 搓(dog):
        dog['hp'] -= dic['ad']
        print('%s 攻击了 %s, %s掉了%s血' % (dic['name'], dog['name'], dog['name'], dic['ad']))

    dic = {
        'name': name,
        'sex': sex,
        'job': job,
        'level': level,
        'hp': hp,
        'weapon': weapon,
        'ad': ad,
        'action':搓,
    }
    return dic

def Dog(name, kind, hp, ad):
    def 舔(person):  # 函数不是一个公共的函数，是一个有归属感的函数（）
        person['hp'] -= dic['ad']
        print('%s 舔了 %s, %s掉了%s血' % (dic['name'], person['name'], person['name'], dic['ad']))

    dic = {
        'name': name,
        'kind': kind,
        'hp': hp,
        'ad': ad,
        'action':舔
    }
    return dic


alex = Person('alex', '不详', '搓澡工', 250, '搓澡巾', 1)
wusir = Person('wusir', 'male', '法师', 500, '打狗棍', 1000)

小白 = Dog('小白', '泰迪', 5000, 249)
小金 = Dog('小金', '柯基', 10000, 499)

小白['action'](alex)
alex['action'](小白)
print(type(alex['action']))
# 1.你怎么保证所有的玩家初始化的时候都拥有相同的属性？
# 2.每来一个新的玩家，我们都自己手动的创建一个字典，然后向字典中填值？
# 3.人和狗的技能如何去写？


# 面向过程: 想要一个结果 写代码 实现计算结果
# 面向对象开发：有哪些角色，角色的属性和技能，两个角色之间是如何交互的

# 复杂的 拥有开放式结局的程序，比较适合使用面向对象开发.
    # 游戏
    # 购物