from django.shortcuts import render
from django.http.response import HttpResponse

class Mug:
    def __init__(self, name, color, description, size, in_use):
        self.name = name
        self.color = color
        self.description = description
        self.size = size
        self.in_use = in_use

mugs = [
    Mug('Monky', 'tan', 'monkey face with handles as ears', 'medium', True),
    Mug('Mickey Mouse', 'white', 'generational mickey mouses on it', 'medium', True),
    Mug('Tea Cup', 'white', 'teacup with fancy edges', 'large', False),
]

# Create your views here.

def home (request):
    return HttpResponse('<h1>We love mugs :D</h1>')

def about(request):
    return render(request, 'about.html')

def mugs_index(request):
    return render(request, 'mugs/index.html', { 'mugs': mugs })