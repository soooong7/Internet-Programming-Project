from django.contrib import admin
from .models import Post, Image

admin.site.register(Post)
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Post.images.through

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
