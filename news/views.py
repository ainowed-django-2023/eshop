from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html', context={
        'page_title': 'News',
        'app': 'index',
        'page': 'news'
    })