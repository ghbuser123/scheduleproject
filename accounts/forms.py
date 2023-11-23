from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # 連携するUserモデル設定
        model = CustomUser

        # フォームで使用するフィールド設定
        fields = ('username','email','password1','password2')