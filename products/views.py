from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import ProductsPost, ColorCategory, SizeCategory, TypeCategory
from .forms import CommentForm

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
            raise PermissionError

def index(request):
    color_categories = ColorCategory.objects.all()
    size_categories = SizeCategory.objects.all()

    return render(request, 'products/purchase_detail.html', {'color_categories': color_categories , 'size_categories': size_categories})
    # return render(request, 'purchase/purchase_detail.html')

def my_view(request):
    color_categories = ColorCategory.objects.all()
    size_categories = SizeCategory.objects.all()

    return render(request, 'products/purchase_detail.html', {'color_categories': color_categories , 'size_categories': size_categories})

def your_form_submission_view(request):
    if request.method == 'POST':
        # 여기에서 폼 데이터를 처리하는 로직을 추가할 수 있습니다.
        return HttpResponse("폼이 성공적으로 제출되었습니다.")
    else:
        return HttpResponse("잘못된 요청입니다.")

def type_page(request, slug):
    type = TypeCategory.objects.get(slug=slug)
    # tags = request.GET.getlist('tags')

    # if tags:
    #     products = ProductsPost.objects.filter(type=type, tags__name__in=tags).distinct()
    # else:
    #     products = ProductsPost.objects.filter(type=type)

    return render(
        request,
        'products/productspost_list.html',
        {
            #'object_list': products,
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
