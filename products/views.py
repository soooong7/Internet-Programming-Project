from django.shortcuts import render
from django.views.generic import ListView

from .models import ColorCategory, SizeCategory, ProductsPost, NumberCategory
from django.http import HttpResponse

# Create your views here.
def index(request):
    size_categories = SizeCategory.objects.all()
    quantity_categories = NumberCategory.objects.all()



    return render(request, 'products/purchase_detail.html', {'quantity_categories': quantity_categories , 'size_categories': size_categories})
    # return render(request, 'products/purchase_detail.html')

def my_view(request):
    size_categories = SizeCategory.objects.all()
    quantity_categories = NumberCategory.objects.all()

    return render(request, 'products/purchase_detail.html', {'quantity_categories': quantity_categories , 'size_categories': size_categories})

def your_form_submission_view(request):
    if request.method == 'POST':
        # 여기에서 폼 데이터를 처리하는 로직을 추가할 수 있습니다.
        return HttpResponse("폼이 성공적으로 제출되었습니다.")
    else:
        return HttpResponse("잘못된 요청입니다.")

class ProductsList(ListView):
    model = ProductsPost
    ordering = '-pk'