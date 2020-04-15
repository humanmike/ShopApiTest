import random
import time

def sleep(n_secs):
    time.sleep(n_secs)

# 生成编辑管理员表单测试数据
def update_user_data():
    data_list = []
    for i in range(10):
        email = 'mail{}@163.com'.format(i)
        mobile = '13111111110'
        data_obj = {
            'email': email,
            'mobile': mobile,
            'verify': '更新成功'
        }
        data_list.append(data_obj)
    return data_list


# 生成添加管理员表单测试数据
def add_user_data():
    data_list = []
    for i in range(10):
        email = 'mail@163.com'
        mobile = '1321111111'.format(i)
        password = '123'
        username = 'lala{}{}'.format(i,i)
        data_obj = {
            'email': email,
            'mobile': mobile,
            'password': password,
            'username': username,
            'verify': '创建成功'
        }
        data_list.append(data_obj)
    return data_list




# 生成已存在添加管理员表单测试数据
def add_exist_user_data():
    data_list = []
    for i in range(10):
        email = 'mail@163.com'
        mobile = '1321111111'.format(i)
        password = '123'
        username = 'jiajia{}{}'.format(i, i)
        data_obj = {
            'email': email,
            'mobile': mobile,
            'password': password,
            'username': username,
            'verify': '用户名已存在'
        }
        data_list.append(data_obj)
    return data_list
