from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mug, Drink
from .forms import DrinkForm

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mugs_index(request):
    mugs = Mug.objects.all()
    return render(request, 'mugs/index.html', { 'mugs': mugs })

def mugs_detail(request, mug_id):
    mug = Mug.objects.get(id=mug_id)
    drink_form = DrinkForm()
    return render(request, 'mugs/detail.html', {'mug': mug, 'drink_form': drink_form})

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