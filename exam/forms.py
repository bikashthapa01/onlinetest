from django import forms
from .models import Subject,Question,Exam


class AddSubjectFrom(forms.ModelForm):

	class Meta:
		model = Subject 
		fields = ('name','description','cover_image')


class AddExamForm(forms.ModelForm):
	class Meta:
		model = Exam 
		fields = ('subject','name')

class AddQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('statments','subject','op_A','op_B','op_C','op_D','correct_op','subject','mark')