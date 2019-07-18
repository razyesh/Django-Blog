from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Post, Category, Subscribe

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')



admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscribe, SubscribeAdmin)
