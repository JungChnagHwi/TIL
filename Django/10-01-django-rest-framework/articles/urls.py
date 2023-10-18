from django.urls import path
from articles import views


urlpatterns = [
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/', views.article_list),
]
