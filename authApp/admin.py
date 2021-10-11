from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.account import Account
admin.site.register(User)
admin.site.register(Account)
