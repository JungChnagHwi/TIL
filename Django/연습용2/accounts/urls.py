from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', views.login ,name='login'),
    path('logout', views.logout ,name='logout'),
    path('delete', views.delete ,name='delete'),
    path('update', views.update ,name='update'),
    path('profile', views.profile ,name='profile'),
    path('signup', views.signup ,name='signup'),
    path('follow', views.follow ,name='follow'),

]