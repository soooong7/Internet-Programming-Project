from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView

from .models import ProductsPost, ColorCategory, SizeCategory, TypeCategory, Comment, NumberCategory
from .forms import CommentForm

# postlist, postdetail 함수
class ProductsList(ListView):
    model = ProductsPost
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['types'] = TypeCategory.objects.all()
        context['colors'] = ColorCategory.objects.all()
        return context

    # 정렬 함수
    def get_queryset(self):
        queryset = super().get_queryset()

        sort_option = self.request.GET.get('sort', None)

        if sort_option == 'low':
            queryset = queryset.order_by('price')
        elif sort_option == 'high':
            queryset = queryset.order_by('-price')
        elif sort_option == 'view':
            queryset = queryset.order_by('-views')

        return queryset

class ProductsDetail(DetailView):
    model = ProductsPost
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductsDetail, self).get_context_data()
        context['types'] = TypeCategory.objects.all()
        context['colors'] = ColorCategory.objects.all()
        context['size_categories'] = SizeCategory.objects.all()
        context['quantity_categories'] = NumberCategory.objects.all()
        context['comment_form'] = CommentForm

        self.object.views += 1
        self.object.save()

        return context

# 카테고리 필터 함수
def type_page(request, slug):
    type = TypeCategory.objects.get(slug=slug)

    return render(
        request,
        'products/productspost_list.html',
        {
            'object_list': ProductsPost.objects.filter(type=type),
            'types': TypeCategory.objects.all(),
            'type': type,
            'colors': ColorCategory.objects.all(),
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
            'types': TypeCategory.objects.all(),
        }
    )

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
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


# 검색 함수
class PostSearch(ProductsList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = ProductsPost.objects.filter(
            Q(name__contains=q) |
            Q(type__type__contains=q) |
            Q(color__color__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context


# 구매 페이지 함수
def your_form_submission_view(request):
    if request.method == 'POST':

        return render(request, 'products/productspost_detail.html', {'success_message': "지금은 구매기간이 아닙니다."})
    else:
        return HttpResponse("잘못된 요청입니다.")

def product_detail(request, product_id):
    product = ProductsPost.objects.get(id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)