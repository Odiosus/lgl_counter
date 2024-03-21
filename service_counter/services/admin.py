from django.contrib import admin

from services.models import Services, Category

admin.site.register(Services, Category)
