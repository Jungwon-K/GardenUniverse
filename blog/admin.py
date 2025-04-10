from django.contrib import admin
from .models import Topic, Post

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('topics',)

admin.site.register(Topic)
admin.site.register(Post)

# Register your models here.
