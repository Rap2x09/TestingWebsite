from django.contrib import admin

from .models import Problem, Dataset

# Register your models here.

admin.site.register(Problem)
admin.site.register(Dataset)