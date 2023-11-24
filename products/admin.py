from django.contrib import admin
from .models import ProductsPost, ProductsTag

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(ProductsPost)
admin.site.register(ProductsTag, TagAdmin)