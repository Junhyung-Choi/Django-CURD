from django.contrib import admin
from .models import Blog,Store,Comment

# Register your models here.

admin.site.register(Blog)
admin.site.register(Store)
admin.site.register(Comment)