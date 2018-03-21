#Author:Santi
from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def get_teachers(request):
    get_list = models.Teachers.objects.all()
    return render(request,'teachers.html',{'get_list':get_list})

def add_teachers(request):
    if request.method == 'GET':
        return render(request,'add_teachers.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        models.Teachers.objects.create(name=name)
        return redirect('teachers.html')

def del_teachers(request):
    nid = request.GET.get('nid')
    models.Teachers.objects.filter(id=nid).delete()
    return redirect('teachers.html')

def edit_teachers(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Teachers.objects.filter(id=nid).values('id','name').first()
        print(obj)
        return render(request,'edit_teachers.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        print(nid,name)
        models.Teachers.objects.filter(id=nid).update(name=name)
        return redirect('teachers.html')

def ajax_teachers(request):
    get_list = models.Teachers.objects.all()
    return render(request,'teachersajax.html',{'get_list':get_list})

def add_ajax_teachers(request):
    import json
    ret = {'status':True,'error':None,'data':None}
    try:
        n = request.POST.get('addname')
        if n != '':
            models.Teachers.objects.create(name=n)
        else:
            ret['status'] = False
            ret['error'] = '数据不能为空'
    except Exception as e:
        ret['status'] = False
        ret['error'] = e
    return HttpResponse(json.dumps(ret))

def teacher_del_ajax(request):
    ret = "exists"
    try:
        nid = request.GET.get('nid')
        models.Teachers.objects.filter(id=nid).delete()
    except Exception as e:
        ret = str(e)
    return HttpResponse(ret)


def editeacherajax(request):
    ret = "succ"
    try:
        name = request.POST.get('name')
        nid = request.POST.get('nid')
        print(name,nid)
        models.Teachers.objects.filter(id=nid).update(name=name)
    except Exception as e:
        ret = 'fail'
    return HttpResponse(ret)


