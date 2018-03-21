#Author:Santi
from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def get_classes(request):
    get_list = models.Classes.objects.all()
    # obj = models.Classes.objects.filter(id=4).first()
    # print("obj",obj.title,obj.m.all())
    # for row in get_list:
    #     print(row.id,row.title,row.m)

    # ret = models.Classes.objects.filter(id=4).values('m__name')
    # print("ret",ret)

    return render(request,'classes.html',{'get_list':get_list})

def add_classes(request):
    if request.method == 'GET':
        teacher_list = models.Teachers.objects.all()
        return render(request,'add_classes.html',locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        teacher_ids = request.POST.getlist('teacher_ids')
        obj = models.Classes(title=title)
        obj.save()
        obj.m.set(teacher_ids)
        return redirect('/classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')


def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('ooxx')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')

def set_teachers(request):
    if request.method == 'GET':
        nid_get = request.GET.get('nid')
        teacher_list = models.Teachers.objects.all()
        current_obj = models.Classes.objects.filter(id=nid_get).first()
        selected_teahcer_list = []
        for teacher in teacher_list:
            if teacher in current_obj.m.all():
                selected_teahcer_list.append(teacher.id)
        return render(request, 'set_teachers.html', locals())
    elif request.method == 'POST':
        nid_post = request.GET.get('nid')
        ids = request.POST.getlist('teahcer_ids')
        post_obj = models.Classes.objects.filter(id=nid_post).first()
        post_obj.m.set(ids)
        return redirect('classes.html')
