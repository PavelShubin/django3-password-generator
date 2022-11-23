from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = 'testing'

    Characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        Characters.extend(string.ascii_uppercase)
    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        Characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def info_about_me(request):
    return render(request, 'generator/information.html')