from django.shortcuts import render

from django.http import HttpResponse


# def home(request):
#     return render(request, 'recipes/home.html')

# example of passing a context to the template
def home(request):
    return render(request, 'recipes/pages/home.html', context={'nome': 'gabriel'})

