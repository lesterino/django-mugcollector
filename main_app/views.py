from django.shortcuts import render
from .models import Mug


# Create your views here.

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mugs_index(request):
    mugs = Mug.objects.all()
    return render(request, 'mugs/index.html', { 'mugs': mugs })

def mugs_detail(request, mug_id):
    mug = Mug.objects.get(id=mug_id)
    return render(request, 'mugs/detail.html', {'mug': mug})