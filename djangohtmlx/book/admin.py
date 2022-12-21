from django.contrib import admin
from .models import *
# Register your models here.
class BookLineAdmin(admin.ModelAdmin):
    model = Book

admin.site.register(Book,BookLineAdmin)


class AuthorAdmin(admin.ModelAdmin):
    model  = Auther



admin.site.register(Auther,AuthorAdmin)
