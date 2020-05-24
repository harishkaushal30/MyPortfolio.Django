from django.urls import  path
from portfolio import views

urlpatterns = [
    path('', views.index, name='home'),
    path('error/', views.error, name='error'),
]