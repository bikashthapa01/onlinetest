from django.shortcuts import render



def indexView(request):
	return render(request,'users/index.html',{})

def loginView(request):
	return render(request,'users/auth/login.html',{})

def registerView(request):
	return render(request,'users/auth/register.html',{})

