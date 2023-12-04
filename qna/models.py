from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=30)
    question=models.TextField()

    head_image = models.ImageField(upload_to='qna/images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('QnApost_detail', args=[str(self.pk)])

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
