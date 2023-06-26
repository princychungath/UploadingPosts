from django.contrib import admin
from .models import PostModel

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','created_date','image']

admin.site.register(PostModel,PostAdmin)