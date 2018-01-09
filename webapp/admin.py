from django.contrib import admin

# Register your models here.
from .models import XgboostModel

admin.site.register(XgboostModel)