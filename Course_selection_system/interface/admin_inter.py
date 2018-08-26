from db import models
from lib import common

admin_log = common.get_logger('admin')


def register_interface(name, pwd):
    admin_obj = models.Admin.get_obj_from_name(name)
    if admin_obj:
        return False, '用户已存在'
    models.Admin(name, pwd)
    admin_log.info('%s 用户注册成功' % name)
    return True, '%s 用户注册成功' % name


def create_school_interface(admin_name, name, address):
    school_obj = models.School.get_obj_from_name(name)
    if school_obj:
        return False, '学校已存在'

    admin_obj = models.Admin.get_obj_from_name(admin_name)
    admin_obj.create_school(name, address)
    admin_log.info('%s 创建了学校 %s' % (admin_name,name))
    return True, '%s 学校创建成功' % name


def create_teacher_interface(admin_name, name):
    teacher_obj = models.Teacher.get_obj_from_name(name)
    if teacher_obj:
        return False, '该老师已存在'
    admin_obj = models.Admin.get_obj_from_name(admin_name)
    admin_obj.create_teacher(name, password='123')
    admin_log.info('%s 创建了老师 %s' % (admin_name,name))
    return True, '%s 老师创建成功' % name


def create_course_interface(admin_name, name, sch_name):
    course_obj = models.Course.get_obj_from_name(name)
    if course_obj:
        return False, '该课程已存在'
    admin_obj = models.Admin.get_obj_from_name(admin_name)
    admin_obj.create_course(name)

    school_obj = models.School.get_obj_from_name(sch_name)
    school_obj.add_course(name)
    admin_log.info('%s 创建了课程 %s' % (admin_name,name))
    return True, '%s 课程创建成功' % name
