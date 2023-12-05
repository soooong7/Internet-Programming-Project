from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import login_view, signup, home_view

urlpatterns = [
    # 빈 경로에 대한 뷰: 로그인 페이지
    path('', login_view, name='login'),

    # 회원가입 페이지에 대한 경로
    path('signup/', signup, name='signup'),

    # 홈 페이지에 대한 경로
    path('home/', home_view, name='home'),

    # 로그아웃
    path('logout/', LogoutView.as_view(next_page="/main/")),
]
