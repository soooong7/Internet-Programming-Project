from django.db import models

# Products Post 모델
class ProductsTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
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

    tags = models.ManyToManyField(ProductsTag, blank=True)

    def __str__(self):
        return f'{self.name}'

