from django.contrib.auth.models import User
from django.db import models

class TypeCategory(models.Model):
    type = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return f'/products/type/{self.slug}/'

    class Meta:
        verbose_name_plural = 'TypeCategories'

class ColorCategory(models.Model):
    color = models.CharField(max_length= 50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return f'/products/color/{self.slug}/'
    class Meta:
        verbose_name_plural = 'ColorCategories'

class SizeCategory(models.Model):
    size = models.CharField(max_length= 50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def __str__(self):
        return self.size
    class Meta:
        verbose_name_plural = 'SizeCategories'

class NumberCategory(models.Model):
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def __str__(self):
        return str(self.quantity)
    class Meta:
        verbose_name_plural = 'NumberCategories'

class ProductsPost(models.Model):
    # 제품명
    name = models.TextField()
    # 제품 가격
    price = models.IntegerField()
    # 제품 사진
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/', blank=True)
    # 제품 상세 사진
    detailimage = models.ImageField(upload_to='products/images/%Y/%m/%d/', blank=True)
    # 제품 조회수
    views = models.PositiveIntegerField(default=0)

    # 제품 태그, 카테고리
    type = models.ManyToManyField(TypeCategory, blank=True) #다대다 (태그 기능)
    color = models.ForeignKey(ColorCategory, null=True, on_delete=models.SET_NULL) #다대일 (카테고리 기능)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f'/products/{self.pk}/'

class Comment(models.Model):
    post = models.ForeignKey(ProductsPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
