from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PaymentDetails(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.IntegerField()
	currency = models.CharField(max_length = 50)
	receipt = models.CharField(max_length = 50)
	orderid = models.CharField(max_length = 100)
	status = models.CharField(max_length = 50)
	subject_code = models.CharField(max_length= 20)

	def __str__(self):
		return self.username

class AssignmentDetails(models.Model):

	colleges = [
	('AMITY', 'Amity'),
	('NMIMS', 'Nmims'),
	]

	assignment_title = models.CharField(max_length=100)
	assignment_description = models.CharField(max_length = 100)
	college = models.CharField(
		max_length=20,
		choices = colleges
		)
	subject = models.CharField(max_length = 50)
	subject_code = models.CharField(max_length= 20, unique = True)
	assignment_file = models.FileField(upload_to = "general_assignments/")

	def __str__(self):
		return self.assignment_title

class RequestedAssignment(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length = 100)
	email = models.EmailField()
	contact_no = models.IntegerField()
	subject_name = models.CharField(max_length=50)
	college = models.CharField(max_length=50)
	special_mention = models.CharField(max_length=500)

	def __str__(self):
		return self.fullname

'''
class MyProfile(models.Model):

	colleges = [
	('AMITY', 'Amity'),
	('NMIMS', 'Nmims'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50)
	college = models.CharField(
		max_length=20,
		choices = colleges
		)
	city = models.CharField(max_length=50)
	contact_no = models.IntegerField()
	email = models.EmailField()

	def save(self, *args, **kwargs):
		if not self.email:
			self.email = self.user.email
		super(MyProfile, self).save(*args, **kwargs)


'''