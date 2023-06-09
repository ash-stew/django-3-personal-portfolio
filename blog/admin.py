from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog) # says want to see this model in the admin