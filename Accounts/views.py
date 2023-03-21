from django.shortcuts import render, redirect
from .Forms import SignUP
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

# Create your views here.
