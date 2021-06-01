from django import forms #form기능 사용
from .models import Post #models에서 post 불러옴

class PostForm(forms.ModelForm): # 지정한 model로 부터 필드를 읽어들어서 PostFields 를 세팅
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body'] #PostFields에 들어갈 Post의 모델 값 