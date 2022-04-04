from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # роут для отображения страницы - Регистрация
    path('reg', views.reg, name='reg'),
    # роут регистрации пользователя
    path('', views.index, name='index'),
]