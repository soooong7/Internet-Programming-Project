from django.urls import path
from . import views
from .views import your_form_submission_view, ProductsList

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('type/<str:slug>/', views.type_page),
    path('color/<str:slug>/', views.color_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('', views.ProductsList.as_view(), name='productspost_list'),
    path('<int:pk>/', views.ProductsDetail.as_view(), name='products_detail'),
    path('your_form_submission/', your_form_submission_view, name='your_form_submission_view'),
    path('get_price/', views.get_price, name='get_price'),
    path('products/', ProductsList.as_view(), name='products_list'),
]