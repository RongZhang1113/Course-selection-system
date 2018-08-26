from db import models
import os
import lib.common
from conf import settings
from lib import common

teacher_log = common.get_logger('admin')


def take_all_course():
    obj = os.path.join(settings.DB_INFO, 'course')
    return lib.common.take_all_dir(obj)


def choose_course_interface(tea_name, cour_name):
    obj = models.Teacher.get_obj_from_name(tea_name)
    if cour_name not in obj.courses:
        obj.add_course(cour_name)
        teacher_log.info('%s 选择了 %s 课程' %(tea_name, cour_name))
        return True, '您选择了[%s]课程' % cour_name
    return False, '您已经选择了该课程'


def check_course_interface(tea_name):
    obj = models.Teacher.get_obj_from_name(tea_name)
    return obj.courses


def check_student_interface(cour_name):
    obj = models.Course.get_obj_from_name(cour_name)
    return obj.students


def modify_score_interface(tea_name, cour_name, stu_name, score):
    tea_obj = models.Teacher.get_obj_from_name(tea_name)
    stu_obj = models.Student.get_obj_from_name(stu_name)
    tea_obj.modify_score(stu_obj, cour_name, score)
    teacher_log.info('%s 给 %s 修改了成绩: %s' %(tea_name, stu_name,score))
    return True, '分数已修改为：%s' % score
