# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# 사용자 인증 폼을 커스터마이징한 클래스
class CustomAuthenticationForm(AuthenticationForm):
    # 사용자명 입력 필드
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    # 비밀번호 입력 필드
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

# 사용자 생성 폼을 커스터마이징한 클래스
class CustomUserCreationForm(UserCreationForm):
    # 이메일 입력 필드
    email = forms.EmailField(required=True, help_text="필수 입력 항목입니다. 유효한 이메일 주소를 입력하세요.")

    class Meta(UserCreationForm.Meta):
        model = User
        # 기본 사용자 생성 폼 필드에 이메일 필드 추가
        fields = UserCreationForm.Meta.fields + ('email',)

    # 비밀번호 검증 메서드 재정의
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        # 사용자 정의 비밀번호 유효성 검사 로직
        # 예: 비밀번호가 최소 8자 이상이어야 함
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 최소 8자 이상이어야 합니다.")

        return password1
