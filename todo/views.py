from django.shortcuts import render
from django.shortcuts import redirect
from .models import Pacient
from django.contrib import messages


def index(request):
    # отображение главной страницы
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def deletePpl(request):
    if request.method == 'POST':
        id_ppl = request.POST['id_ppl']
        Pacient.objects.filter(id=id_ppl).delete()
        return redirect('reg')
    return redirect('reg')


def createPpl(request):
    if request.method == 'POST':
        sname = request.POST['second_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        bday = request.POST['bday']
        if (bday != '') & (sname != '') & (fname != '') & (lname != ''):
            Pacient.objects.create(
            name=fname,
            second_name=sname,
            last_name=lname,
            date_b=bday,
        )
            messages.error(request, 'Пациент успешно зарегистрирован', extra_tags='safe')
            return redirect('reg')
        else :
            return redirect('reg')
    else:
        return redirect('reg')


def reg(request):
    # отображение страницы регистрации
    pacient_all = Pacient.objects.all()
    return render(request, 'reg.html', {
        'title': 'Регистрация',
        'pacient_all': pacient_all,
    })


def dateof(request):
    # отображение страницы регистрации
    return render(request, 'dateof.html', {
        'title': 'Дата обращения',
    })


def employes(request):
    # отображение страницы регистрации
    return render(request, 'employes.html', {
        'title': 'Сотрудники',
    })



