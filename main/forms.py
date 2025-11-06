from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 사용자에게 입력받을 필드만 지정
        fields = ['image', 'caption']
