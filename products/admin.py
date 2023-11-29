from django.contrib import admin
from .models import ColorCategory, NumberCategory, SizeCategory, TypeCategory, ProductsPost

class ColorCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'color']
    # prepopulated_fields = 추가
    prepopulated_fields = {'slug': ('color', )}

class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'size']
    prepopulated_fields = {'slug': ('size',)}

class NumberCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity']
    prepopulated_fields = {'slug': ('quantity',)}

class TypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    prepopulated_fields = {'slug': ('type',)}


admin.site.register(ProductsPost)
admin.site.register(ColorCategory, ColorCategoryAdmin)
admin.site.register(NumberCategory, NumberCategoryAdmin)
admin.site.register(SizeCategory, SizeCategoryAdmin)
admin.site.register(TypeCategory, TypeCategoryAdmin)




