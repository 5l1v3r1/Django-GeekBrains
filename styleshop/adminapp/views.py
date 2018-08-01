from django.shortcuts import render

def create(request):

    return render(request, 'adminapp/form.html', {})
