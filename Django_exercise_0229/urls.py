"""Django_exercise_0229 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from app01.views import Classes,Tearchers,Students,Search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login', views.login),
    # url(r'^test', views.CBV.as_view()),
    url(r'^teachers.html$', Tearchers.get_teachers),
    url(r'^add_teachers.html', Tearchers.add_teachers),
    url(r'^del_teachers.html', Tearchers.del_teachers),
    url(r'^edit_teachers.html', Tearchers.edit_teachers),

    url(r'^classes.html$', Classes.get_classes),
    url(r'^add_classes.html$', Classes.add_classes),
    url(r'^del_classes.html$', Classes.del_classes),
    url(r'^edit_classes.html', Classes.edit_classes),
    url(r'^set_teachers.html', Classes.set_teachers),
    url(r'^students.html', Students.get_students),
    url(r'^add_students.html', Students.add_students),
    url(r'^del_students.html', Students.del_students),
    url(r'^edit_students.html', Students.edit_students),

    url(r'^teachersajax.html$', Tearchers.ajax_teachers),
    url(r'^addteachersajax.html$', Tearchers.add_ajax_teachers),
    url(r'^teacher_del_ajax.html$', Tearchers.teacher_del_ajax),
    url(r'^editeacherajax.html$', Tearchers.editeacherajax),

    url(r'^search', Search.search),

]
