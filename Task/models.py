from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
# Create your models here.




class UserInfo(models.Model):
	"""docstring for UserInfo"""
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True,max_length=50)
	phone = models.CharField(max_length=10,unique=True,validators=[RegexValidator(regex='^.{10}$', message='Input 10 digit phone number', code='phonerror')])
	dob = models.DateField(default=datetime.now)



	def __str__(self):
		return self.name


class Choices(models.Model):
	"""docstring for Choices"""
	name = models.CharField(max_length=50,unique=True)

	def __str__(self):
		return self.name


class Question(models.Model):
	"""docstring for Question"""
	answer_type_choice = [('input_box','input_box'),('select_box','select_box')]

	question = models.TextField()
	required = models.BooleanField(default=True)
	created_on = models.DateTimeField(default=datetime.now)
	answer_type = models.CharField(max_length=50,default='input',choices=answer_type_choice)
	options = models.ManyToManyField(Choices,blank=True)


	def __str__(self):
		return self.question

	class Meta(object):
		"""docstring for Meta"""
		ordering = ['id']
			


		
class UserResponse(models.Model):
	"""docstring for UserResponse"""
	user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer = models.TextField(blank=True,null=True,default='Not Answered')

	def __str__(self):
		return self.user.name


