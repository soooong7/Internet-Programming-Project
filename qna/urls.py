from django.urls import path
from . import views
from .views import created_post

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('qna_detail/<int:pk>/', views.PostDetail.as_view(), name='qna_detail'),
    path('qna_list/', views.PostList.as_view(), name='qna_list'),
    path('<int:pk>/new_comment/', views.new_comment),
    path('created_post/', views.PostCreate.as_view()),
    path('qna_detail/<int:pk>/new_comment/', views.new_comment, name='new_comment'),
    path('', views.fna),
]