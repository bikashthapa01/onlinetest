from django.shortcuts import render

# Create your views here.

def newExam(request):
	return render(request,'addexam.html',{})
	