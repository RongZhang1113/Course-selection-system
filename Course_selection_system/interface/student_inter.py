from db import models
from lib import common

student_log = common.get_logger('admin')


def register_interface(name, pwd):
    obj = models.Student.get_obj_from_name(name)
    if obj:
        return False, '用户已存在'
    models.Student(name, pwd)
    student_log.info('%s 学员注册成功' % name)
    return True, '%s 学员注册成功' % name


def choose_school_interface(stu_name, school_name):
    obj = models.Student.get_obj_from_name(stu_name)
    school = obj.get_school()
    if school:
        return False, '您已经选择了学校'
    obj.choose_school(school_name)
    student_log.info('%s 加入了 %s 学校' % (stu_name, school_name))
    return True, '您成功加入了%s' % school_name


def take_choose_course_interface(stu_name):
    obj = models.Student.get_obj_from_name(stu_name)
    if obj.school:
        school_obj = models.School.get_obj_from_name(obj.school)
        if school_obj.courses:
            return True, school_obj.courses
        return False, '该学校下暂无课程'
    return False, '请先选择学校'


def choose_course_interface(stu_name, cou_name):
    obj = models.Student.get_obj_from_name(stu_name)
    if cou_name in obj.courses:
        return False, '您已经选择了本门学科'

    obj.choose_course(cou_name)
    cou_obj = models.Course.get_obj_from_name(cou_name)
    cou_obj.add_student(stu_name)
    student_log.info('%s 选择了 %s 课程' % (stu_name, cou_name))
    return True, '您成功选择了%s课程' % cou_name


def check_score_interface(stu_name):
    obj = models.Student.get_obj_from_name(stu_name)
    return obj.scores
