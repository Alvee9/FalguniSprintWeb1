from django.contrib import admin

# Register your models here.

from .models import User, Poll_admin

admin.site.register(User)
admin.site.register(Poll_admin)

