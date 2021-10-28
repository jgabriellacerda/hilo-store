from django.shortcuts import render, HttpResponse
from core.models import Product

# Create your views here.

def hello(request, nome):
    return HttpResponse(f'Hello {nome}')

def home(request):
    return render(request, 'model-home.html', {})

def shop(request):
    products = Product.objects.all()
    response = {'products':products}
    return render(request, 'model-shop.html', response)

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def confirmation(request):
    return render(request, 'confirmation.html', {})

def product_single(request):
    return render(request, 'product-single.html', {})

def shop_sidebar(request):
    return render(request, 'shop-sidebar.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def coming_soon(request):
    return render(request, 'coming-soon.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def order(request):
    return render(request, 'order.html', {})

def address(request):
    return render(request, 'address.html', {})

def profile_details(request):
    return render(request, 'profile-details.html', {})

def login(request):
    return render(request, 'login.html', {})

def signin(request):
    return render(request, 'signin.html', {})

def forget_password(request):
    return render(request, 'forget-password.html', {})

def error_404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

# def pages(request):
#     return render(request, 'pages.html')

# def blog(request):
#     return render(request, 'blog.html')

# def elements(request):
#     return render(request, 'elements.html')