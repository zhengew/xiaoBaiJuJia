# 对象() 调用这个了类中的 __call__方法
class A:pass
class B:
    def __call__(self, *args, **kwargs):
        pass

print(callable(A))  # True
print(callable(B))  # True
print(callable(A())) # False
print(callable(B())) # True