from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('login/', views.register_view, name='login'),
    path('login/home/', views.home, name='home'),
]
