from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    notice_image = models.ManyToManyField('image.Image')

    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Image(models.Model):
    image = models.ImageField(upload_to='notice/images/%y/%m/%d/')
