from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout as user_logout
from .models import User
from django.contrib.auth.decorators import login_required



def indexView(request):
	return render(request,'users/index.html',{})

def loginView(request):
	if request.method == "POST":
		usn = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=usn,password=password)

		if user is not None:
			login(request,user)
			return redirect('dashboard')
		else:
			return render(request,'users/auth/login.html',{'msg':'Incorrect login Det ails'})

		
	return render(request,'users/auth/login.html',{})

def registerView(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('success')
	return render(request,'users/auth/register.html',{'form':form})

@login_required
def dashboard(request):
	return render(request,'users/dashboard/dashboard.html')


def success(request):
	return render(request,'users/auth/success.html')

def logout(request):
	user_logout(request)
	return redirect('index')

