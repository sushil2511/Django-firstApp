from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    context = {
        'title' : 'First app',
        'content' : 'This is content of app'
    }
    return render(request, 'index.html', context=context)