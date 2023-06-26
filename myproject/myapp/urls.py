from django.urls import path
from . import views
urlpatterns = [
    path('', views.my_home_view, name='home'),
    path('signup/', views.MySignUpView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('create-post/', views.create_my_post, name='addpost'),
    path('post-list/', views.my_post_list, name='viewpost'),
   
   
]
