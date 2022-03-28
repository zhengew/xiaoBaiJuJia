from core import src

def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
    :param f:
    :return:
    '''
    def inner(*args, **kwargs):
        # 访问函数前进行三次登陆认证
        flag = 3
        if src.status_dict['status']:
            ret = f(*args, **kwargs)
            flag = 0
            return ret
        else:
            print("请先登陆用户")
        # 第一次验证失败，继续验证2次
        while flag > 1:
            if src.status_dict['status']:
                ret = f(*args, **kwargs)
                return ret

            elif flag <= 1:
                print("超过认证次数")
            flag -= 1

    return inner