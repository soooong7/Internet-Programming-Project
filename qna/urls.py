from django.urls import path
from . import views
from .views import qna_detail



urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('qna_detail/', qna_detail, name='qna_detail'),
]