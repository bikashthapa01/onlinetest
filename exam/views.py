from django.shortcuts import render

# Create your views here.

def newExam(request):
	return render(request,'exam.html',{})

def addQuestion(request):
	return render(request,'question.html',{})

def addSubject(request):
	return render(request,'subject.html',{})
	
def ranks(request):
	pass 
def marks(request):
	pass 

	