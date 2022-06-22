from django.contrib import admin

# Register your models here.
#@0622
from django.contrib import admin
from .models import Post

admin.site.register(Post)
