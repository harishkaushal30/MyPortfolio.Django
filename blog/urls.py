from django.urls import  path
from blog import views
import blog

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:pk>/', views.blog_detail, name="blog_detail"),
    path('<category>/', views.blog_category, name="blog_category"),
]

handler404 = blog.views.handler404
handler500 = blog.views.handler500
