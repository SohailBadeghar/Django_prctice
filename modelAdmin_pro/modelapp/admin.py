from django.contrib import admin
from modelapp.models import StudentDetails
# Register your models here.
@admin.register(StudentDetails)
class StudentAdmin(admin.ModelAdmin):  
    list_display = ('Roll_no','Name','Email','division','password')

# admin.site.register(StudentDetails,StudentAdmin)