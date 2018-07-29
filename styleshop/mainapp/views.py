from django.shortcuts import render

def checkout(request):
    return render(request, 'mainapp/checkout.html')
    
def contact(request):
    return render(request, 'mainapp/contact.html')
    
def shop(request):
    return render(request, 'mainapp/shop.html')
    
def single_product_details(request):
    return render(request, 'mainapp/single-product-details.html')
    