from django.shortcuts import render
from .forms import AddSubjectFrom,AddExamForm,AddQuestionForm

# Create your views here.

def exam(request):
	return render(request,'exam.html',{})

def question(request):
	return render(request,'question.html',{})

def subject(request):
	return render(request,'subject.html',{})






def addExam(request):
	if request.method == 'POST':
		form = AddExamForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = AddExamForm()
	return render(request,'add_exam.html',{'form':form})

def addQuestion(request):
	if request.method == 'POST':
		form = AddQuestionForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = AddQuestionForm()
	return render(request,'add_question.html',{'form':form})

def addSubject(request):
	if request.method == 'POST':
		form = AddSubjectFrom(request.POST)
		if form.is_valid():
			form.save()
			msg = 'Saved.'
			form = AddSubjectFrom()
	else:
		msg = ''
		form = AddSubjectFrom()
	return render(request,'add_subject.html',{'form':form},{'msg':msg})
	
def ranks(request):
	pass 
def marks(request):
	pass 

	