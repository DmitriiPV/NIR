from django.shortcuts import render


def index(request):
    # отображение главной страницы
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def reg(request):
    # отображение страницы регистрации
    # user_form = UReg()
    return render(request, 'reg.html', {
        'title': 'Регистрация',
        # 'create_user': user_form,
    })


def auth(request):
    # отображение страницы авторизации
    # if not request.user.is_authenticated:
        return render(request, 'auth.html', {
            'title': 'Авторизация',
        })
    # else:
    #     return redirect(user_profile)

