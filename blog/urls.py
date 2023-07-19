from django.urls import path,include
from . import views
# from views import *  to import 

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.About, name='about'),
    path('blog/', views.Blog, name='blog' ),
    path('news/', views.News, name='news' ),
    path('contact/', views.Contact, name='contact' ),
]