from django.contrib import admin
from .models import user, profile, chat
admin.site.register(user)
admin.site.register(profile)
admin.site.register(chat)
# Register your models here.
