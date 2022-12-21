from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title__istartswith',]
    autocomplete_fields = ['author']

admin.site.register(Post, PostAdmin)
