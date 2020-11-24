from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'blog/index.html', data)


def info(request):
    return render(request, 'blog/info.html')
