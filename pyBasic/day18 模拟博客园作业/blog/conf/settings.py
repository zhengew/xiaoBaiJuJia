# 保存注册用户信息 格式为 用户名|密码|
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
register_path = os.path.join(BASE_PATH, 'db', 'register')