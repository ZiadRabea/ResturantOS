from django.shortcuts import render
from .models import *

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignUP
from django.contrib.auth import authenticate, login


def sign_up(request):
    if request.method == 'POST':
        Form = SignUP(request.POST)
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data['username']
            password = Form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(f'/')
    else:
        Form = SignUP()
    return render(request, 'registration/sign_up.html', {'Form': Form})


def profile(request, id):
    p = Profile.objects.get(id=id)
    context = {
        "profile": p,
    }
    return render(request, "pages/Profile.html", context)

