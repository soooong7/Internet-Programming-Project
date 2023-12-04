
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'qna/QnApost_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'qna/QnApost_detail.html'

def your_view_function(request):
    post = Post.objects.first()

    url = post.get_absolute_url()

    # 나머지 뷰 로직
    return render(request, 'QnApost_list.html', {'post': post, 'url': url})

#def QnApost_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    #return render(request, 'QnApost_detail.html', {'post': post})

def qna_detail(request):
    return render(request, 'QnApost_detail.html', context)