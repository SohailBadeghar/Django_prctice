from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)

class studentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_no','password','repassword']