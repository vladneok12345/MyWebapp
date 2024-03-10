from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    #path('',views.PostListView.as_view(),name='PostListView'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.profile, name='profile'),
    path('', views.home, name="home"),
]