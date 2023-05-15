from django.shortcuts import render


def sign_up(request):
    return render(request, 'accounts/sign_up.html', context={
        'page_title': 'Sign-Up',
        'app': 'sign_up',
        'page': 'accounts'
    })


def sign_in(request):
    return render(request, 'accounts/sign_in.html', context={
        'page_title': 'Sign-In',
        'app': 'sign_in',
        'page': 'accounts'
    })


def sign_out(request):
    return render(request, 'accounts/sign_out.html', context={
        'page_title': 'Sign-Out',
        'app': 'sign_out',
        'page': 'accounts'
    })


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'page_title': 'Profile',
        'app': 'profile',
        'page': 'accounts'
    })