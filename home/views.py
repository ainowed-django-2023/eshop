from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', context={
        'page_title': 'Main',
        'app': 'index',
        'page': 'home'
    })


def about(request):
    return render(request, 'home/about.html', context={
        'page_title': 'About',
        'app': 'about',
        'page': 'home'
    })


def contacts(request):
    return render(request, 'home/contacts.html', context={
        'page_title': 'Contacts',
        'app': 'contacts',
        'page': 'home'
    })

