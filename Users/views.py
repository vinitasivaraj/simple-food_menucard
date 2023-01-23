from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.
def Register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welocme {username},Account has been created!!')
            form.save()
            return redirect('login')
    else:
            form = RegisterForm()
    return render(request,'Users/register.html',{'form':form})


@login_required()
def profile(request):
    return render(request,'Users/profile.html')