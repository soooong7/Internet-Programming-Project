# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    email = forms.EmailField(required=True, help_text="필수 입력 항목입니다. 유효한 이메일 주소를 입력하세요.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@duksung.ac.kr'):
            raise ValidationError("등록이 허용된 이메일 도메인은 @duksung.ac.kr 입니다.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        # 사용자 정의 패스워드 유효성 검사 로직 추가
        # 예시: 패스워드가 최소 8자 이상이어야 함
        if len(password1) < 8:
            raise forms.ValidationError("비밀번호는 최소 8자 이상이어야 합니다.")

        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # 비밀번호 일치 여부 확인
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
