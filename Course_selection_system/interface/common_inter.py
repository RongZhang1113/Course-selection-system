from db import models
import os
import lib.common
from conf import settings


def login_interface(name, password, user_type):
    if user_type == 'admin':
        obj = models.Admin.get_obj_from_name(name)
    elif user_type == 'student':
        obj = models.Student.get_obj_from_name(name)
    elif user_type == 'teacher':
        obj = models.Teacher.get_obj_from_name(name)
    else:
        return False, '没有该类型'
    if obj:
        if obj.password == password:
            return True, '%s:%s 登录成功' % (user_type, name)
        return False, '密码错误，请重试'
    return False, '用户不存在'


def take_all_school():
    obj_path = os.path.join(settings.DB_INFO, 'school')
    return lib.common.take_all_dir(obj_path)
