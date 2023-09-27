from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True, upload_to ='images/') # media 안에 상세경로 설정
    image = models.ImageField(blank=True, upload_to ='%Y/%m/%d/') # media 안에 날짜명으로 세부경로 생성
    # False면 모든 게시글 쓸 때마다 넣어야 함, 공백 허용은 안 넣어도 상관없다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
