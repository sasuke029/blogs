

from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def About(request):
    return render(request,'blog/about.html')

def Blog(request):
    return render(request,'blog/blog.html')

def News(request):
    return render(request,'blog/news.html')

def Contact(request):
    return render(request,'blog/contact.html')

# Create your views here.
