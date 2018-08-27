import os
from conf import settings
import logging.config


def login_auth(user_type):
    '''
    验证登录装饰器
    :param user_type: admin, student, teacher
    :return: func(*args, **kwargs)
    '''
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
    '''
    拿到工程的文件路径
    :param path: 
    :return: 
    '''
    if os.path.exists(path):
        obj_dir = os.listdir(path)
        return obj_dir
    return False


def get_logger(name):
    '''
    用于拿到日志字典，记录日志
    :param name: 
    :return: 
    '''
    logging.config.dictConfig(settings.LOGGING_DIC)
    my_log = logging.getLogger(name)
    return my_log
