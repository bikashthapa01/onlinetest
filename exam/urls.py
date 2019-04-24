from django.urls import path
from . import views

urlpatterns = [
	path('',views.exam,name="all_exam"),
	path('questions/',views.question,name="all_question"),
	path('subjects/',views.subject,name="all_subject"),
	path('add/new/',views.addExam,name="add_exam"),
	path('add/subject/',views.addSubject,name="add_subject"),
	path('add/question/',views.addQuestion,name="add_question"),
]