from django.shortcuts import render, redirect
from messDel.models import user, userAuth
from django.http import HttpResponse, HttpResponseRedirect
import hashlib, os
from django.core.mail import send_mail
from django.urls import reverse

def userLogin(request):
	if request and request.method=='POST' :
		password = request.POST["password"]
		emailid = request.POST["emailid"]
		password = hashlib.sha224(password.encode('utf-8')).hexdigest()
		if password and emailid :	
			if user.objects.count() > 0 :
				if user.objects.filter(email = emailid).exists() :
					passwordActual = user.objects.get(email = emailid).password
					if passwordActual == password :
						if user.objects.get(email = emailid).emailauth == True :
							return render(request, 'messDel/msg.html')
						else :
							hashEmail = hashlib.sha224(emailid.encode('utf-8')).hexdigest()
							userP = user.objects.get(email = emailid)
							time = str(userP.timeCreation.hour) + ":" + str(userP.timeCreation.minute) + ":" + str(userP.timeCreation.second)
							hashTime = hashlib.sha224((time).encode('utf-8')).hexdigest()
							hashC = hashlib.sha224((hashTime+hashEmail).encode('utf-8')).hexdigest()
							body = 'To verify its you please click the link below :\n ' + 'http://127.0.0.1:8000/' + 'emailauth/' + hashC + '/' + '\n \n Report this issue : \n' + 'http://127.0.0.1:8000/' + 'wrongEmail/' + hashC + '/'
							send_mail('Verification MessageDel',body,'shubhendrapalsinghal@gmail.com',[emailid], fail_silently=False)
							userP.emailkey = hashC
							userP.save()
							return render(request,'messDel/verify.html')
					else :
						return render(request, 'messDel/error.html')
			elif user.objects.count() == 0 or ~user.objects.filter(email = emailid).exists() :
				user.objects.create(password = password, email = emailid).save()
				hashEmail = hashlib.sha224(emailid.encode('utf-8')).hexdigest()
				userP = user.objects.get(email = emailid)
				time = str(userP.timeCreation.hour) + ":" + str(userP.timeCreation.minute) + ":" + str(userP.timeCreation.second)
				hashTime = hashlib.sha224((time).encode('utf-8')).hexdigest()
				hashC = hashlib.sha224((hashTime+hashEmail).encode('utf-8')).hexdigest()
				body = 'To verify its you please click the link below :\n ' + 'http://127.0.0.1:8000/' + 'emailauth/' + hashC + '/' + '\n \n Report this issue : \n' + 'http://127.0.0.1:8000/' + 'wrongEmail/' + hashC + '/'
				send_mail('Verification MessageDel',body,'shubhendrapalsinghal@gmail.com',[emailid], fail_silently=False)
				userP.emailkey = hashC
				userP.save()
				return render(request, 'messDel/verify.html')
		else :
			return render(request, 'messDel/index.html')
	else :
		return render(request, 'messDel/index.html')

def emailAuth(request, auth) :
	userP = user.objects.get(emailkey = auth)
	userP.emailauth = True
	userP.save()
	if userAuth.objects.count() > 0 :
		if userAuth.objects.get(email = userP.email) :
			return HttpResponseRedirect(reverse(userProfile, args=(auth,)))
	elif userAuth.objects.count() == 0 or ~userAuth.objects.get(email = userP.email) : 		
		userAuth.objects.create(email = userP).save()
		return HttpResponseRedirect(reverse(userProfile, args=(auth,)))


def userProfile(request, auth): 
	if request and request.method == 'POST' :
		username = request.POST["username"]
		status = request.POST["status"]
		if username and status :
			userP = user.objects.get(emailkey = auth)
			userA = userAuth.objects.get(email = userP.email)
			userA.username = username
			userA.status = status
			userA.save()
	return render(request, 'messDel/msg.html/')

def googleRedirect(request) :
	return render(request, 'messDel/msg.html')

def wrongEmail(request, auth) :
	userP = user.objects.get(emailkey = auth)
	userP.delete()
	return render(request,'messDel/thanks.html')