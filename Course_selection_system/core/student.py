from interface import common_inter, student_inter
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
            flg, msg = student_inter.register_interface(name, pwd)
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
        flg, msg = common_inter.login_interface(name, pwd, 'student')
        if flg:
            print(msg)
            user_data['name'] = name
            break
        else:
            print(msg)


@login_auth(user_type='student')
def choose_school():
    print('选择学校')
    school_list = common_inter.take_all_school()
    if school_list:
        for k, v in enumerate(school_list):
            print('%s:%s' % (k, v))
        choice = input('请选择学校或按(q/Q)退出>>:').strip()
        if choice == 'q' or choice == 'Q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                flg, msg = student_inter.choose_school_interface(user_data['name'], school_list[choice])
                if flg:
                    print(msg)
                else:
                    print(msg)
            else:
                print('选择错误，请重试')
        else:
            print('必须输入数字')


@login_auth(user_type='student')
def choose_course():
    print('选择课程')
    while True:
        flg, courses_list = student_inter.take_choose_course_interface(user_data['name'])
        if not flg:
            print(courses_list)
            return
        for k, v in enumerate(courses_list):
            print('%s:%s' % (k, v))
        choice = input('请选择课程或按(q/Q)退出>>>>:').strip()
        if choice == 'q' or choice == 'Q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice <= len(courses_list):
                # continue
                _, msg = student_inter.choose_course_interface(user_data['name'], courses_list[choice])
                print(msg)
                break
            else:
                print('选择错误，请重试')
        else:
            print('必须输入数字')


@login_auth(user_type='student')
def check_score():
    print('查看分数')
    score = student_inter.check_score_interface(user_data['name'])
    print(score)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def student_view():
    while True:
        time.sleep(0.1)
        print('''
        1 注册
        2 登录
        3 选择学校
        4 选择课程
        5 查看分数
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
