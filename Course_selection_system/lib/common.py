import os
from conf import settings
import logging.config


def login_auth(user_type):
    from core import admin, student, teacher
    def auth(func):
        def wrapper(*args, **kwargs):
            if user_type == 'admin':
                if not admin.user_data['name']:
                    print('请先登录')
                    admin.login()
                    if admin.user_data['name']:
                        return func(*args, **kwargs)
                    return
                return func(*args, **kwargs)

            elif user_type == 'student':
                if not student.user_data['name']:
                    print('请先登录')
                    student.login()
                    if student.user_data['name']:
                        return func(*args, **kwargs)
                    return
                return func(*args, **kwargs)

            elif user_type == 'teacher':
                if not teacher.user_data['name']:
                    print('请先登录')
                    teacher.login()
                    if teacher.user_data['name']:
                        return func(*args, **kwargs)
                    return
                return func(*args, **kwargs)

        return wrapper

    return auth


def take_all_dir(path):
    if os.path.exists(path):
        obj_dir = os.listdir(path)
        return obj_dir
    return False


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    my_log = logging.getLogger(name)
    return my_log
