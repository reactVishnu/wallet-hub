from django.contrib import admin
from .models import Detail
from django.contrib.auth import get_user_model
# Register your models here.

admin.site.register(Detail)
admin.site.register(get_user_model())
