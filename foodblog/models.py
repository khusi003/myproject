from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10,blank=True)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    otp = models.IntegerField(default = 459)
    pic=models.FileField(upload_to='foodbolg/img/',default='foodbolg/img/avatar.png')

class Review(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE)  
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
     
class Gallary(models.Model):
    pic=models.FileField(upload_to='foodbolg/img/')
    