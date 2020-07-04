from django.db import models

class user(models.Model):
	password = models.CharField(max_length=8)
	email = models.EmailField(primary_key = True)
	timeCreation = models.DateTimeField(auto_now_add = True)
	lastSeenTime = models.DateTimeField(auto_now = True)
	emailkey = models.TextField()
	emailauth = models.BooleanField(default=False)

class userAuth(models.Model):
	email = models.ForeignKey(user, on_delete = models.CASCADE)
	username = models.CharField(max_length = 15,default = None, null = True)
	status = models.CharField(max_length = 30, default = "Available" , null = True)
	photo  = models.ImageField(upload_to = 'profilePhotos/', default = 'profilePhotos/default.jpg', null = True)

class profile(models.Model):
	email = models.ForeignKey(user,on_delete=models.CASCADE)
	interest = models.CharField(max_length=30)

class chat(models.Model):
	user1 = models.ForeignKey(user,on_delete=models.CASCADE, related_name='user1')
	user2 = models.ForeignKey(user,on_delete=models.CASCADE, related_name='user2')
	message = models.TextField()
# Create your models here.
