from django.db import models
from users.models import User

# Create your models here.


class Subject(models.Model):
	name 			= models.CharField(max_length=255)
	description 	= models.TextField()
	cover_image 	= models.CharField(max_length=1000,blank=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	choice = (('A','A'),('A','B'),('A','C'),('D','D'))
	subject 	= models.ForeignKey(Subject,on_delete=models.CASCADE)
	statments 	= models.TextField()
	op_A 	= models.CharField(max_length=1000)
	op_B 	= models.CharField(max_length=1000)
	op_C 	= models.CharField(max_length=1000)
	op_D 	= models.CharField(max_length=1000)
	correct_op 	= models.CharField(choices=choice,max_length=10)
	mark 		= models.CharField(max_length=10)
	def __str__(self):
		return self.statments


class Exam(models.Model):
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	name = models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.name

class Mark(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
	total_marks = models.CharField(max_length=10)
	def __str__(self):
		return self.total_marks

# # class Rank(models.Model):
# # 	pass 
