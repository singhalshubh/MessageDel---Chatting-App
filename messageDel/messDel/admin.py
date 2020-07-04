from django.contrib import admin
from .models import user, profile, chat, userAuth
admin.site.register(user)
admin.site.register(profile)
admin.site.register(chat)
admin.site.register(userAuth)
# Register your models here.
