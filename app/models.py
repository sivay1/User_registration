from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Userdata(AbstractUser):
	first_name = models.CharField(max_length= 30,blank = True)
	last_name = models.CharField(max_length= 30,blank = True)
	profile_picture = models.ImageField(upload_to='profile_pics/',blank = True)
	address_line = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=255, blank=True)
	state = models.CharField(max_length=255, blank=True)
	pincode = models.CharField(max_length=10, blank=True)
