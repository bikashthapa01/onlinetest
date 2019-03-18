from django.shortcuts import render
from .forms import RegisterForm



def indexView(request):
	return render(request,'users/index.html',{})

def loginView(request):
	if request.method == "POST":
		print("POST REQUEST DETECTED.")
	return render(request,'users/auth/login.html',{})

def registerView(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request,'users/auth/register.html',{'form':form})


