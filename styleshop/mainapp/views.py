from django.shortcuts import render

def checkout(request):
    return render(request, 'mainapp/checkout.html')
    
def contact(request):
    return render(request, 'mainapp/contact.html')
    