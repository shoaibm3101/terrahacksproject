from django.contrib import admin
from .models import Question, Company, Profile

# Register your models here.
admin.site.register(Question)
admin.site.register(Company)
admin.site.register(Profile)