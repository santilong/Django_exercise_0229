#Author:Santi
from django.shortcuts import HttpResponse,render,redirect
from app01 import models

def get_students(request):
    students_list = models.Student.objects.all()
    return render(request,'students.html',{'students_list':students_list})

def add_students(request):
    if request.method == 'GET':
        classes_list = models.Classes.objects.all()
        return render(request,'add_students.html',{'classes_list':classes_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/students.html')


def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/students.html')

def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).first()
        classes_list = models.Classes.objects.values('id','title')
        return render(request,'edit_students.html',{'obj':obj,'classes_list':classes_list})
