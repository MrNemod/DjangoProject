from django.contrib import admin
from .models import allergens, item, category

# Register your models here.
admin.site.register(allergens)
admin.site.register(item)
admin.site.register(category)