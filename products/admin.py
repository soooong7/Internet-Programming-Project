from django.contrib import admin
from .models import ProductsPost, CategoryTag, ColorTag


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductsPost)
admin.site.register(CategoryTag, CategoryAdmin)
admin.site.register(ColorTag, ColorAdmin)

