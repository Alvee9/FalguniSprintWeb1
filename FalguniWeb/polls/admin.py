from django.contrib import admin

# Register your models here.

from .models import User, Poll_admin, PM, Mayor, Councillor

admin.site.register(User)
admin.site.register(Poll_admin)
admin.site.register(PM)
admin.site.register(Mayor)
admin.site.register(Councillor)
