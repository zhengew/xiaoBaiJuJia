from conf import settings
from lib import common
status_dict = {
    'username': None,
    'status': False,
}



def get_user_pwd():
	user_dict = {}
	with open(settings.register_path, encoding='utf-8') as f:
		for line in f:
			line_list = line.strip().split('|')
			user_dict[line_list[0].strip()] = line_list[1].strip()
	return user_dict


def login():
    u_dict = get_user_pwd()
    count = 1
    while count < 4:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in u_dict and password == u_dict[username]:
            print('登录成功')
            status_dict['username'] = username
            status_dict['status'] = True
            return True
        else:
            print('用户名密码错误....重新登录')
        count += 1


def register():
    pass


@common.auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')

@common.auth
def comment():
    print('欢迎访问评论页面')

@common.auth
def dariy():
    print('欢迎访问日记页面')

@common.auth
def collections():
    print('欢迎访问收藏页面')

def login_out():
    pass

def _quit():
    pass



# 下面写法不好
# while 1:
#     print('''
#     1.请登录
#     2.请注册
#     3.进入文章页面
#     4.进入评论页面
#     5.进入日记页面
#     6.进入收藏页面
#     7.注销账号
#     8.退出整个程序
#     ''')
#     num = input('请输入序号:').strip()
#     if num == '1':
#         login()
#     elif num == '2':
#         register()


dic = {
    1: login,
    2: register,
    3: article,
    4: comment,
    5: dariy,
    6: collections,
    7: login_out,
    8: _quit,
}

def run():
    while 1:
        print('''
            1.请登录
            2.请注册
            3.进入文章页面
            4.进入评论页面
            5.进入日记页面
            6.进入收藏页面
            7.注销账号
            8.退出整个程序
            ''')
        num = input('请输入选项').strip()
        num = int(num)
        dic[num]()

run()