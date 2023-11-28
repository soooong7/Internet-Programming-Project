from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductsPost, CategoryTag, ColorTag


class ProductsList(ListView):
    model = ProductsPost
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryTag.objects.all()
        context['color'] = ColorTag.objects.all()

        return context

def products_list(request):
    selected_categories = request.GET.getlist('category')
    selected_color = request.GET.get('color')

    queryset = ProductsPost.objects.all()

    if selected_categories:
        category_filter = Q()
        for category in selected_categories:
            category_filter |= Q(category__id=category)
        queryset = queryset.filter(category_filter)

    if selected_color:
        queryset = queryset.filter(color__id=selected_color)

    context = {
        'products': queryset,
    }

    return render(request, 'products/productspost_list.html', context)