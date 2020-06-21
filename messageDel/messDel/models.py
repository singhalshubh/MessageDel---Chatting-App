from django.db import models

class user(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=8)
	email = models.EmailField()
	timeCreation = models.DateTimeField(auto_now_add = True)
	lastSeenTime = models.DateTimeField(auto_now = True)
	emailkey = models.TextField()
	emailauth = models.BooleanField(default=False)

class profile(models.Model):
	email = models.ForeignKey(user,on_delete=models.CASCADE)
	interest = models.CharField(max_length=30)

class chat(models.Model):
	user1 = models.ForeignKey(user,on_delete=models.CASCADE, related_name='user1')
	user2 = models.ForeignKey(user,on_delete=models.CASCADE, related_name='user2')
	message = models.TextField()
# Create your models here.
