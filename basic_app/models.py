from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Organization = models.CharField(max_length=50,blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
	Name = models.CharField(max_length=100,null = True)
	Email = models.EmailField(max_length=100, null = True)
	Organization = models.CharField(max_length=100,null = True)
	Message = models.TextField(max_length=300, null=True)
	Date = models.DateTimeField(default=date.today,editable=False, null=False, blank=False)
	def __str__(self):
 		return '%s %s'%(self.Name, self.Organization)	
