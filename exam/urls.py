from django.urls import path
from . import views

urlpatterns = [
	path('add/new/',views.newExam,name="add_exam"),
	path('add/question/',views.addQuestion,name="add_question"),
	path('add/subject/',views.addSubject,name="add_subject"),
]