from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .forms import CommentForm

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'qna/QnApost_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'qna/QnApost_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'question', 'head_image', 'file_upload', 'category']
    template_name = 'qna/QnApost_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/qna/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'question', 'head_image', 'file_upload', 'category']

    template_name = 'qna/QnApost_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def your_view_function(request):
    post = Post.objects.first()

    url = post.get_absolute_url()

    # 나머지 뷰 로직
    return render(request, 'QnApost_list.html', {'post': post, 'url': url})

def fna(request):
    posts = Post.objects.all()

    return render(
        request,
        'qna/fna.html',
        {
            'posts': posts,
        }
    )

def qna_detail(request):
    return render(request, 'QnApost_detail.html')

def created_post(request):
    post = Post.objects.get()
    return render(request, 'created_post.html')

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_aboslute_url())
    else:
        raise PermissionDenied