from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def registration(request):
    USFO=UserForm()
    PFO=ProfileForm()
    d={'USFO':USFO,'PFO':PFO}
    if request.method =='POST' and request.FILES:
       UFDO = UserForm(request.POST)
       PFDO = ProfileForm(request.POST,request.FILES)
       if UFDO.is_valid() and PFDO.is_valid():
           MUFDO = UFDO.save(commit=False)
           MUFDO.set_password(UFDO.cleaned_data['password'])
           MUFDO.save()

           MPFDO = PFDO.save(commit=False)
           MPFDO.username=MUFDO
           MPFDO.save()
           return HttpResponse('Registration is Succesfully....')
    return render(request,'registration.html',d)
