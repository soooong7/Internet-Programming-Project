from django.urls import path
from . import views
from .views import index, my_view, your_form_submission_view, ProductsList, type_page, color_page

app_name= 'purchase'

urlpatterns = [
    #path('', views.index),
    #path('', index, name='index'),
    #path('my-view/', my_view, name='my-view'),
    #path('your_form_submission/', your_form_submission_view, name='your_form_submission_view'),
    path('type/<str:slug>/', views.type_page),
    path('color/<str:slug>/', views.color_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.ProductsDetail.as_view()),
    path('', views.ProductsList.as_view()),
]