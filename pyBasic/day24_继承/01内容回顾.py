# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求
# 外圆面积-内圆面积(圆周率X大半径的平方-圆周率X小半径的平方\圆周率X（大半径的平方-小半径的平方）)。
# 公式：S环=π（R²-r²）。公式：S环=π(R+r)(R-r)=π(R+r)d，d为圆环的宽度。
# from math import pi
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return pi * self.r ** 2
#
#     def perimeter(self):
#         return 2 * pi * self.r
#
# class Ring:
#     def __init__(self, outer_r, inner_r):
#         outer_r, inner_r = (outer_r, inner_r) if outer_r > inner_r else (inner_r, outer_r)
#         self.out_r = Circle(outer_r)
#         self.in_c = Circle(inner_r)
#
#     def area(self):
#         return self.out_r.area() - self.in_c.area()
#
#     def perimeter(self):
#         return self.out_r.perimeter() + self.in_c.perimeter()
#
#
# r1 = Ring(10, 8)
# print(r1.perimeter())

# 1.传递的半径大小的顺序问题
# 2.为什么要用组合

# 程序里有两个需求：和圆形和环形相关，求环形相关的内容的时候用到了圆的公示


'''
命名空间：
    # 在类的命名空间里：静态变量和绑定方法
    # 在对象的命名空间里：类指针 对象的属性（实例变量）

    # 调用习惯
        # 类名.静态变量
        # 对象.静态变量（对象调用静态变量的时候，不能对变量进行赋值操作， 对象.静态变量 = 123）

        # 绑定方法
            # 对象.绑定方法()  # ==> 类名.绑定方法(对象)

        # 对象.实例变量

# 组合
    # 一个类的对象是另一个类的对象的属性
    # 两个类之间有什么有关系的地方：例如 班级有学生  学生有班级 班级有课程 图书有作者 学生有成绩

    # 学生 和 课程
    # 班级 和 课程
    # 圆形 和 圆环
'''