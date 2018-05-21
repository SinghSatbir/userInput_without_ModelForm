from django.contrib import admin

# Register your models here.
from app_users.models import User

admin.site.register(User)