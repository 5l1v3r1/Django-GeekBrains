from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def blog(request):
    return render(request, 'mainapp/blog.html')
    
def checkout(request):
    return render(request, 'mainapp/checkout.html')
    
def contact(request):
    return render(request, 'mainapp/contact.html')
    
def regular_page(request):
    return render(request, 'mainapp/regular-page.html')
    
def shop(request):
    return render(request, 'mainapp/shop.html')
    
def single_blog(request):
    return render(request, 'mainapp/single-blog.html')
    
def single_product_details(request):
    return render(request, 'mainapp/single-product-details.html')
    