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
        return f'/productes/color/{self.slug}/'
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

    # 제품 태그, 카테고리
    type = models.ManyToManyField(TypeCategory, blank=True)
    color = models.ForeignKey(ColorCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'/products/{self.pk}/'
