from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webpages/index.html')

def categories(request):
    return render(request, 'webpages/categories.html')

def community(request):
    return render(request, 'webpages/community.html')

def signout(request):
    return render(request, 'webpages/welcome.html')