from django.shortcuts import redirect
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('hello/<nome>/', views.hello),
    path('', RedirectView.as_view(url='/home/'), name='home'),
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('product-single/<product_id>/', views.product_single, name='product-single'),
    path('shop-sidebar/', views.shop_sidebar, name='shop-sidebar'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    path('faq/', views.faq, name='faq'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order/', views.order, name='order'),
    path('address/', views.address, name='address'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user, name='logout_user'),
    path('signin/', views.signin, name='signin'),
    path('forget-password/', views.forget_password, name='forget-password'),

]