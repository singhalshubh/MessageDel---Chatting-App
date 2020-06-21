from django.shortcuts import render
from messDel.models import user
from django.http import HttpResponse
import hashlib, os
from django.core.mail import send_mail

def userLogin(request):
	if request and request.method=='POST' :
		username = request.POST["username"]
		password = request.POST["password"]
		emailid = request.POST["emailid"]
		password = hashlib.sha224(password.encode('utf-8')).hexdigest()
		if username and password and emailid :	
			if user.objects.count() > 0 :
				if user.objects.filter(email = emailid).exists() :
					passwordActual = user.objects.get(email = emailid).password
					if passwordActual == password :
						if user.objects.get(email = emailid).emailauth == True :
							return render(request, 'messDel/msg.html')
						else :
							return render(request,'messDel/verify.html')
					else :
						return render(request, 'messDel/error.html')
				else :
					user.objects.create(username = username, password = password, email = emailid).save()
					hashEmail = hashlib.sha224(emailid.encode('utf-8')).hexdigest()
					hashUsername = hashlib.sha224(username.encode('utf-8')).hexdigest()
					userP = user.objects.get(email = emailid)
					time = str(userP.timeCreation.hour) + ":" + str(userP.timeCreation.minute) + ":" + str(userP.timeCreation.second)
					hashTime = hashlib.sha224((time).encode('utf-8')).hexdigest()
					hashC = hashlib.sha224((hashTime+hashEmail+hashUsername).encode('utf-8')).hexdigest()
					body = 'https://127.0.0.1/' + 'emailauth/' + hashC + '/'
					send_mail('Verification MessageDel',body,'shubhendrapalsinghal@gmail.com',emailid, fail_silently=False)
					userP.emailkey = hashC
					userP.save()
					return render(request, 'messDel/verify.html')
			else :
				user.objects.create(username = username, password = password, email = emailid).save()
				hashEmail = hashlib.sha224(emailid.encode('utf-8')).hexdigest()
				hashUsername = hashlib.sha224(username.encode('utf-8')).hexdigest()
				userP = user.objects.get(email = emailid)
				time = str(userP.timeCreation.hour) + ":" + str(userP.timeCreation.minute) + ":" + str(userP.timeCreation.second)
				hashTime = hashlib.sha224((time).encode('utf-8')).hexdigest()
				hashC = hashlib.sha224((hashTime+hashEmail+hashUsername).encode('utf-8')).hexdigest()
				body = 'http://127.0.0.1:8000/' + 'emailauth/' + hashC + '/'
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
	return render(request, 'messDel/sample.html')
