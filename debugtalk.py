
import time

def sleep(n_secs):
    time.sleep(n_secs)

# 生成添加表单测试数据
def add_user_data():
    data_list = []
    for i in range(10):
        email = 'mail@163.com'
        mobile = '1321111111'.format(i)
        password = '123'
        username = 'ceshi{}{}'.format(i,i)
        data_obj = {
            'email': email,
            'mobile': mobile,
            'password': password,
            'username': username,
            'verify': '创建成功'
        }
        data_list.append(data_obj)
    return data_list


