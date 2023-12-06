# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse

from .forms import CustomUserCreationForm

def home_view(request):
    """
    홈 페이지를 렌더링하는 뷰 함수
    """
    return render(request, 'home.html')

def login_view(request):
    """
    로그인 페이지를 렌더링하고, 유효한 로그인 시 홈 페이지로 리다이렉트하는 뷰 함수
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/main/')  # 로그인 후 리다이렉트할 URL을 설정하세요
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect

def signup(request):
    """
    회원가입 페이지를 렌더링하고, 유효한 회원가입 시 로그인 페이지로 리다이렉트하는 뷰 함수
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 성공 시 로그인 페이지로 리다이렉트
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()

    # 유효하지 않은 경우, 현재 페이지에 머무르고 오류 메시지를 템플릿에 전달
    return render(request, 'login.html', {'form': form})
