from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            password=request.POST['password1']
            user=authenticate(request,username=username,password=password)
            user.is_staff = True
            user.save()
            login(request,user)
            return redirect('blog-home')
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request,'users/register.html',context)
from django.http import JsonResponse
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
