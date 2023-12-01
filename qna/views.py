from django.views.generic import ListView, DetailView
from .models import QnAPost

class PostList(ListView):
    model = QnAPost
    ordering = '-pk'

class PostDetail(DetailView):
    model = QnAPost
