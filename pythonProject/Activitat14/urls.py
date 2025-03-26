from django.urls import path
from . import views

urlpatterns = [
    path('', views.inici, name='inici'),
    path('login/', views.login_vista, name='login_vista'),
]
