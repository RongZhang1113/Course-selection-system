from interface import admin_inter, common_inter
from lib.common import login_auth
import time

user_data = {'name': None}


def register():
    print('注册')
    if user_data['name']:
        print('您已登录,无需注册')
        return
    while True:
        name = input('请输入用户名或按(q/Q)退出>>:').strip()
        if name == 'q' or name == 'Q':
            return
        if len(name) == 0:
            print('用户名不能为空')
            continue
        pwd = input('请输入密码>>:').strip()
        con_pwd = input('请再次输入密码>>:').strip()
        if pwd == con_pwd:
            flg, msg = admin_inter.register_interface(name, pwd)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def login():
    print('登录')
    if user_data['name']:
        print('您已登录')
        return
    while True:
        name = input('请输入用户名或按(q/Q)退出>>:').strip()
        if name == 'q' or name == 'Q':
            return
        if len(name) == 0:
            print('用户名不能为空')
            continue
        pwd = input('请输入密码>>:').strip()
        flg, msg = common_inter.login_interface(name, pwd, 'admin')
        if flg:
            print(msg)
            user_data['name'] = name
            break
        else:
            print(msg)


@login_auth(user_type='admin')
def create_school():
    print('创建学校')
    while True:
        name = input('请输入学校名或按(q/Q)退出>>:').strip()
        if name == 'q' or name == 'Q':
            return
        if len(name) == 0:
            print('用户名不能为空')
            continue
        address = input('请输入学校地址或按(q/Q)退出>>:').strip()
        if address == 'q' or address == 'Q':
            return
        flg, msg = admin_inter.create_school_interface(user_data['name'], name, address)
        if flg:
            print(msg)
            break
        else:
            print(msg)


@login_auth(user_type='admin')
def create_teacher():
    print('创建老师')
    while True:
        name = input('请输入教师名或按(q/Q)退出>>:').strip()
        if name == 'q' or name == 'Q':
            return
        if len(name) == 0:
            print('用户名不能为空')
            continue
        flg, msg = admin_inter.create_teacher_interface(user_data['name'], name)
        if flg:
            print(msg)
            break
        else:
            print(msg)


@login_auth(user_type='admin')
def create_course():
    print('创建课程')
    while True:
        school_list = common_inter.take_all_school()
        if school_list:
            for k, v in enumerate(school_list):
                print('%s:%s' % (k, v))
            choice = input('请先选择学校或按(q/Q)退出>>:').strip()
            if choice == 'q' or choice == 'Q':
                return
            if choice.isdigit():
                choice = int(choice)
                if choice <= len(school_list):
                    name = input('请输入课程名或按(q/Q)退出>>:').strip()
                    if name == 'q' or name == 'Q':
                        return
                    if len(name) == 0:
                        print('不能为空')
                        continue
                    flg, msg = admin_inter.create_course_interface(user_data['name'], name, school_list[choice])
                    if flg:
                        print(msg)
                        break
                    else:
                        print(msg)
                else:
                    print('选择错误，请重试')
            else:
                print('必须输入数字')


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}


def admin_view():
    while True:
        time.sleep(0.1)
        print('''
        1 注册
        2 登录
        3 创建学校
        4 创建老师
        5 创建课程
        0 返回上一层
        ''')
        choice = input('请选择>>:').strip()
        if choice == '0':
            global user_data
            user_data['name'] = None
            break
        if choice not in func_dic:
            print('输入错误，请重试')
            continue
        func_dic[choice]()
