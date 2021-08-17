from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mug
# from django.views.generic import ListView

# class MugList(ListView):
#     model = Mug
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

class MugCreate(CreateView):
    model = Mug
    fields = '__all__'
    success_url = '/mugs/'

class MugUpdate(UpdateView):
    model = Mug
    fields = '__all__'

class MugDelete(DeleteView):
    model = Mug
    success_url = '/mugs/'