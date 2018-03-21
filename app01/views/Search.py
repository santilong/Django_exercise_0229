#Author:Santi
from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def search(reqeust):
    ##################正向查询：从Student表通过跨表查询ID为1的学生所在的班级：##################
    # ret = models.Student.objects.filter(id=5).values('cs__title')
    obj = models.Student.objects.filter(id=1).first()
    ret = obj.cs.title
    ##################反向查询：从Class表通过跨表查询ID为1的课程的学生：##################
    ###一###
    # obj = models.Classes.objects.filter(title='Linux基础').first()
    ###二###
    # ret = obj.student_set.all()
    # print(ret)
    # ret = obj.ssss.all()
    # for row in ret:
    #     print(row.username, row.id, row.age, row.gender)
    # ret = models.Classes.objects.filter(title='Linux基础').values('ssss__username','ssss__age')
    # ret = models.Classes.objects.filter(title='Linux基础').values('student__username','student__age')
    print(ret)
    return HttpResponse('...')