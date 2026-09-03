from django.contrib import admin
from .models import allergens, item, itemImage, category

# Register your models here.
admin.site.register(allergens)
admin.site.register(category)

class ItemImageInline(admin.TabularInline):
    model = itemImage
    extra = 1
    max_num = 5
@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]
    list_display = ('name', 'price', 'category')