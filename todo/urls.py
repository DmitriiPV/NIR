from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # роут для отображения страницы - Регистрация нового пациента
    path('reg', views.reg, name='reg'),
    # роут Домашней страницы
    path('', views.index, name='index'),
    # роут для отображения страницы - Дата обращения
    path('dateof', views.dateof, name='dateof'),
    # роут для отображения страницы - Сотрудники
    path('employes', views.employes, name='employes'),
]
