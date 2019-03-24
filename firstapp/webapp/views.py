from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        'title' : 'First app',
        'content' : 'This is content of app'
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')