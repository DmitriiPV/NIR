from django.shortcuts import render
from django.shortcuts import redirect
from .models import Pacient, Special, Skill, Employes, Diagnosis, DateOf
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


def doctorspecial(request):
    if request.method =='POST':
        pac = request.POST['pac']
        vrac = request.POST['vrac']
        diagn = request.POST['diagn']
        dday = request.POST['dday']
        pac_id = Pacient.objects.get(id=pac)
        vrac_id = Employes.objects.get(id=vrac)
        diagn_id = Diagnosis.objects.get(id=diagn)
        skill_id = Employes.objects.get(id=vrac).skill.id
        koef = Skill.objects.get(id=skill_id).koef
        cost= Diagnosis.objects.get(id=diagn).cost
        print(skill_id)
        print(koef)
        print(cost)
        if (pac != '') & (vrac != '') & (diagn != '') & (dday != ''):
            DateOf.objects.create(
                pacient=pac_id,
                emp=vrac_id,
                diag=diagn_id,
                dateoft=dday,
                costh=float(koef)*int(cost)
            )
            return redirect('dateof')
        else :
            return redirect('dateof')
    return redirect('dateof')


def deletedate(request):
    if request.method == 'POST':
        id_dto = request.POST['id_dto']
        DateOf.objects.filter(id=id_dto).delete()
        return redirect('dateof')
    return redirect('dateof')

def dateof(request):
    # отображение страницы регистрации
    pacient_all = Pacient.objects.all()
    emp_all = Employes.objects.all()
    diag_all = Diagnosis.objects.all()
    dateof_all = DateOf.objects.all()
    # id = request.session.get('id')
    # if (id != '') :
    #     per = Employes.objects.get(id=id).special.id
    #     dia = Diagnosis.objects.filter(special=per).all()
    #     print(per)
    #     return render(request, 'dateof.html', {
    #         'title': 'Дата обращения',
    #         'pacient_all': pacient_all,
    #         'emp_all': emp_all,
    #         'diag_all': diag_all,
    #         'dia': dia,
    #     })
    # else :
    return render(request, 'dateof.html', {
            'title': 'Дата обращения',
            'pacient_all': pacient_all,
            'emp_all': emp_all,
            'diag_all': diag_all,
            'dateof_all' : dateof_all,
        })

def deleteEmp(request):
    if request.method == 'POST':
        id_emp = request.POST['id_emp']
        Employes.objects.filter(id=id_emp).delete()
        return redirect('employes')
    return redirect('employes')


def createEmp(request):
    if request.method == 'POST':
        sname = request.POST['second_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        special = request.POST['special']
        skill = request.POST['skill']
        skill_id = Skill.objects.get(id=skill)
        special_id = Special.objects.get(id=special)
        if (special != '') & (skill != '') & (sname != '') & (fname != '') & (lname != ''):
            Employes.objects.create(
            name=fname,
            second_name=sname,
            last_name=lname,
            special=special_id,
            skill=skill_id,
        )
            messages.error(request, 'Сотрудник успешно зарегистрирован', extra_tags='safe')
            return redirect('employes')
        else :
            return redirect('employes')
    else:
        return redirect('employes')


def employes(request):
    # отображение страницы регистрации
    special_all = Special.objects.all()
    skill_all = Skill.objects.all()
    employes_all = Employes.objects.all()
    return render(request, 'employes.html', {
        'title': 'Сотрудники',
        'special_all': special_all,
        'skill_all': skill_all,
        'employes_all': employes_all,
    })



