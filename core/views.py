from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse(f'Hello {nome}')

def home(request):
    return render(request, 'index.html', {})

def shop(request):
    return render(request, 'shop.html', {})

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