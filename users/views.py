from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request):
    uf=1
    pf=1
    if request.method=="POST":
        uf=UserUpdateForm(request.POST,instance=request.user)
        pf=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uf.is_valid() and pf.is_valid():
            uf.save()
            pf.save()
            return redirect('profile')
    else:
        uf=UserUpdateForm(instance=request.user)
        pf=ProfileUpdateForm(instance=request.user.profile)
    return render(request,'users/profile.html',{'uf':uf,'pf':pf})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"success")
            return redirect('login')
    else:
        form=UserRegisterForm()    
    return render(request,'users/register.html',{'form':form})