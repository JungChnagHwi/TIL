from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length = 10)
#     content = forms.CharField(widget = forms.Textarea)
    #인풋 두 개 만든 것          #위젯 - 인풋의표현만 바꿀 뿐

#Form - 사용자 입력 데이터를 DB 에 저장하지 않을 때(로그인 등)
#ModelForm - 사용자 입력 데이터를 DB 에 저장할 때(게시글 , 회원가입 등)
class ArticleForm(forms.Modelform):
    class Meta: #메타데이터는 어떤 데이터에 대한 데이터,, 여기서 메타는 알티클의 정보에 대한 정보
        model = Article
        fields = '__all__'
        # fields = ('title',) 
        # exclude = ('title',)