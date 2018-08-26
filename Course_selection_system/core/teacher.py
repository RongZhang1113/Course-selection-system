from interface import common_inter, teacher_inter
from lib.common import login_auth
import time

user_data = {'name': None}


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
        flg, msg = common_inter.login_interface(name, pwd, 'teacher')
        if flg:
            print(msg)
            user_data['name'] = name
            break
        else:
            print(msg)


@login_auth(user_type='teacher')
def choose_course():
    print('选择课程')
    course = teacher_inter.take_all_course()
    if not course:
        print('暂时没有课程，请联系管理员')
        return
    for k, v in enumerate(course):
        print('%s:%s' % (k, v))
    choice = input('请选择课程或按(q/Q)退出>>:').strip()
    if choice == 'q' or choice == 'Q':
        return
    if choice.isdigit():
        choice = int(choice)
        if choice < len(course):
            flg, msg = teacher_inter.choose_course_interface(user_data['name'], course[choice])
            if flg:
                print(msg)
            else:
                print(msg)
        else:
            print('选择错误，请重试')
    else:
        print('必须输入数字')


@login_auth(user_type='teacher')
def check_course():
    print('查看课程')
    course = teacher_inter.check_course_interface(user_data['name'])
    if course:
        for info in course:
            print(info)
    else:
        print('请先选择课程')


@login_auth(user_type='teacher')
def check_student():
    print('查看学生')
    course = teacher_inter.check_course_interface(user_data['name'])
    if course:
        for k, v in enumerate(course):
            print('%s:%s' % (k, v))
        choice = input('请选择课程查看学生或按(q/Q)退出>>:').strip()
        if choice == 'q' or choice == 'Q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course):
                student_list = teacher_inter.check_student_interface(course[choice])
                for k, v in enumerate(student_list):
                    print('%s:%s' % (k, v))
            else:
                print('选择存在的课程查看')
        else:
            print('必须输入数字')
    else:
        print('您还没选择所教的课程')


@login_auth(user_type='teacher')
def modify_score():
    print('修改成绩')
    course = teacher_inter.check_course_interface(user_data['name'])
    if course:
        for k, v in enumerate(course):
            print('%s:%s' % (k, v))
        choice = input('请先选择课程或按(q/Q)退出>>:').strip()
        if choice == 'q' or choice == 'Q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course):
                student_list = teacher_inter.check_student_interface(course[choice])
                for k, v in enumerate(student_list):
                    print('%s:%s' % (k, v))
                choose = input('请选择学生>>:').strip()
                if choose.isdigit():
                    choose = int(choose)
                    if choose < len(student_list):
                        score = input('请输入要修改成的分数>>:').strip()
                        if score.isdigit():
                            score = int(score)
                            flg, msg = teacher_inter.modify_score_interface(user_data['name'], course[choice],
                                                                            student_list[choose], score)
                            print(msg)
                        else:
                            print('必须输入数字')
                    else:
                        print('选择错误，请重试')
                else:
                    print('必须输入数字')
            else:
                print('选择错误，请重试')
        else:
            print('必须输入数字')
    else:
        print('请先选择课程')


func_dic = {
    '1': login,
    '2': check_student,
    '3': choose_course,
    '4': check_course,
    '5': modify_score
}


def teacher_view():
    while True:
        time.sleep(0.1)
        print('''
        1 登录
        2 查看学生
        3 选择课程
        4 查看课程
        5 修改分数
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
