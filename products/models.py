from django.db import models

class CategoryTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class ColorTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class ProductsPost(models.Model):
    # 제품명
    name = models.TextField()
    # 제품 가격
    price = models.IntegerField()
    # 제품 사진
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/', blank=True)

    # 제품 태그 (카테고리, 색상)
    category = models.ManyToManyField(CategoryTag, related_name='category_tag', blank=True)
    color = models.ForeignKey(ColorTag, related_name='color_tag', blank=True, null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'