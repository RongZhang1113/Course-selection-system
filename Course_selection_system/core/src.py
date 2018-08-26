from core import admin, student, teacher
import time

func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view
}


def run():
    while True:
        time.sleep(0.1)
        print('''
        1 管理员视图
        2 学生视图
        3 老师视图
        0 退出程序
        ''')
        choice = input('请选择>>:').strip()
        if choice == '0': break
        if choice not in func_dic:
            print('输入错误，请重试')
            continue
        func_dic[choice]()
