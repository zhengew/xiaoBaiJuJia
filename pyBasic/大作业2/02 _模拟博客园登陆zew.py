status_dict = {
    'username': None,
    'status': False,
}

register_path = r'D:\python_22\day18\blog\register'

def get_user_pwd():



def login():



def register():
    pass


def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
    :param f:
    :return:
    '''



@auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')

@auth
def collections():
    print('欢迎访问收藏页面')

def login_out():
    pass

def _quit():
    pass