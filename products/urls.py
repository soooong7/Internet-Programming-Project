from django.urls import path
from . import views
from .views import index, my_view , your_form_submission_view,   ProductsList

app_name= 'products'

urlpatterns = [
    path('', views.index),
    path('', index, name='index'),
    path('my-view/', my_view, name='my-view'),
    path('your_form_submission/', your_form_submission_view, name='your_form_submission_view'),