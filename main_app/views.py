from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Mug, Drink, Coaster
from .forms import DrinkForm

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

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mugs_index(request):
    mugs = Mug.objects.all()
    return render(request, 'mugs/index.html', { 'mugs': mugs })

def mugs_detail(request, mug_id):
    mug = Mug.objects.get(id=mug_id)
    coasters_mug_doesnt_have = Coaster.objects.exclude(id__in = mug.coasters.all().values_list('id'))
    drink_form = DrinkForm()
    return render(request, 'mugs/detail.html', {
        'mug': mug, 
        'drink_form': drink_form,
        'coasters': coasters_mug_doesnt_have
        })

def add_drink(request, mug_id):
    form = DrinkForm(request.POST)
    if form.is_valid():
        new_drink = form.save(commit=False)
        new_drink.mug_id = mug_id
        new_drink.save()
    return redirect('detail', mug_id=mug_id)

def delete_drink(request, mug_id, drink_id):
    mug = Mug.objects.get(id=mug_id)
    drink = Drink.objects.get(mug_id=mug_id, id=drink_id)
    mug.drink_set.remove(drink)
    return redirect('detail', mug_id=mug_id)

class CoasterList(ListView):
    model = Coaster

class CoasterDetail(DetailView):
    model = Coaster

class CoasterCreate(CreateView):
    model = Coaster
    fields = '__all__'

class CoasterUpdate(UpdateView):
    model = Coaster
    fields = ['color', 'shape']

class CoasterDelete(DeleteView):
    model = Coaster
    success_url = '/coasters/'

def assoc_coaster(request, mug_id, coaster_id):
    Mug.objects.get(id=mug_id).coasters.add(coaster_id)
    return redirect('detail', mug_id=mug_id)