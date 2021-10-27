from django.urls import path
from . import views

urlpatterns = [
    path('hello/<nome>/', views.hello),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    # path('pages', views.pages, name='pages'),
    # path('blog', views.blog, name='blog'),
    # path('elements', views.elements, name='elements'),
]