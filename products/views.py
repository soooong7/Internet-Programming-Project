from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView

from .models import ProductsPost, ColorCategory, SizeCategory, TypeCategory, Comment
from .forms import CommentForm, SortForm


class ProductsList(ListView):
    model = ProductsPost
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['types'] = TypeCategory.objects.all()
        context['colors'] = ColorCategory.objects.all()
        return context


class ProductsDetail(DetailView):
    model = ProductsPost
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductsDetail, self).get_context_data()
        context['types'] = TypeCategory.objects.all()
        context['colors'] = ColorCategory.objects.all()
        context['comment_form'] = CommentForm
        return context


# 댓글 함수
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(ProductsPost, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(post.get_absoulte_url())
        else:
            raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)  # 인자로 받은 pk값과 같은 pk값을 가진 댓글을 쿼리셋으로 받아오기
    post = comment.post  # 해당 댓글이 달린 포스트를 저장. 리다이렉트 용도
    if request.user.is_authenticated and request.user == comment.author:  # 방문자가 로그인했는지, 해당 댓글의 작성자인지 확인
        comment.delete()
        return redirect(post.get_absolute_url())  # 댓글이 달려있던 포스트의 상세 페이지로 리다이렉트
    else:
        raise PermissionDenied


def index(request):
    color_categories = ColorCategory.objects.all()
    size_categories = SizeCategory.objects.all()

    return render(request, 'products/purchase_detail.html',
                  {'color_categories': color_categories, 'size_categories': size_categories})
    # return render(request, 'purchase/purchase_detail.html')


def my_view(request):
    color_categories = ColorCategory.objects.all()
    size_categories = SizeCategory.objects.all()

    return render(request, 'products/purchase_detail.html',
                  {'color_categories': color_categories, 'size_categories': size_categories})


def your_form_submission_view(request):
    if request.method == 'POST':
        # 여기에서 폼 데이터를 처리하는 로직을 추가할 수 있습니다.
        return HttpResponse("폼이 성공적으로 제출되었습니다.")
    else:
        return HttpResponse("잘못된 요청입니다.")


def type_page(request, slug):
    type = TypeCategory.objects.get(slug=slug)
    # tags = request.GET.getlist('tags')

    return render(
        request,
        'products/productspost_list.html',
        {
            # 'object_list': products,
            'object_list': ProductsPost.objects.filter(type=type),
            'types': TypeCategory.objects.all(),
            'type': type,
        }
    )


def color_page(request, slug):
    color = ColorCategory.objects.get(slug=slug)

    return render(
        request,
        'products/productspost_list.html',
        {
            'object_list': ProductsPost.objects.filter(color=color),
            'colors': ColorCategory.objects.all(),
            'color': color,
        }
    )
