from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #
    path('deletePpl', views.deletePpl, name='deletePpl'),
    #
    path('createPpl', views.createPpl, name='createPpl'),
    # роут для отображения страницы - Регистрация нового пациента
    path('reg', views.reg, name='reg'),
    # роут Домашней страницы
    path('', views.index, name='index'),
    #
    path('doctorspecial', views.doctorspecial, name='doctorspecial'),
    #
    path('deletedate', views.deletedate, name='deletedate'),
    # роут для отображения страницы - Дата обращения
    path('dateof', views.dateof, name='dateof'),
    #
    path('deleteEmp', views.deleteEmp, name='deleteEmp'),
    #
    path('createEmp', views.createEmp, name='createEmp'),
    # роут для отображения страницы - Сотрудники
    path('employes', views.employes, name='employes'),
    #
    path('creatediag', views.creatediag, name='creatediag'),
    #
    path('createspec', views.createspec, name='createspec'),
    #
    path('deleteddd', views.deleteddd, name='deleteddd'),
    #
    path('deletesss', views.deletesss, name='deletesss'),
    #
    path('diagspec', views.diagspec, name='diagspec')
]
