from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('register/',views.register,name='register'),
    path('login', views.loginpage,name= 'login'),
    path('logout', views.LogoutView, name= 'logout'),
    path('delete/<str:name>/', views.DeleteTask, name = 'delete'),
    path('update/<str:name>/', views.UpdateTask, name ='update'),

]
