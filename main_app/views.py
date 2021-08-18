from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mug, Drink, Coaster
from .forms import DrinkForm

class MugCreate(LoginRequiredMixin, CreateView):
    model = Mug
    fields = '__all__'
    success_url = '/mugs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MugUpdate(LoginRequiredMixin, UpdateView):
    model = Mug
    fields = '__all__'

class MugDelete(LoginRequiredMixin, DeleteView):
    model = Mug
    success_url = '/mugs/'

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def mugs_index(request):
    mugs = Mug.objects.filter(user=request.user)
    mugs = request.user.mug_set.all()
    return render(request, 'mugs/index.html', { 'mugs': mugs })

@login_required
def mugs_detail(request, mug_id):
    mug = Mug.objects.get(id=mug_id)
    coasters_mug_doesnt_have = Coaster.objects.exclude(id__in = mug.coasters.all().values_list('id'))
    drink_form = DrinkForm()
    return render(request, 'mugs/detail.html', {
        'mug': mug, 
        'drink_form': drink_form,
        'coasters': coasters_mug_doesnt_have
        })

@login_required
def add_drink(request, mug_id):
    form = DrinkForm(request.POST)
    if form.is_valid():
        new_drink = form.save(commit=False)
        new_drink.mug_id = mug_id
        new_drink.save()
    return redirect('detail', mug_id=mug_id)

@login_required
def delete_drink(request, mug_id, drink_id):
    mug = Mug.objects.get(id=mug_id)
    drink = Drink.objects.get(mug_id=mug_id, id=drink_id)
    mug.drink_set.remove(drink)
    return redirect('detail', mug_id=mug_id)

class CoasterList(LoginRequiredMixin, ListView):
    model = Coaster

class CoasterDetail(LoginRequiredMixin, DetailView):
    model = Coaster

class CoasterCreate(LoginRequiredMixin, CreateView):
    model = Coaster
    fields = '__all__'

class CoasterUpdate(LoginRequiredMixin, UpdateView):
    model = Coaster
    fields = ['color', 'shape']

class CoasterDelete(LoginRequiredMixin, DeleteView):
    model = Coaster
    success_url = '/coasters/'

@login_required
def assoc_coaster(request, mug_id, coaster_id):
    Mug.objects.get(id=mug_id).coasters.add(coaster_id)
    return redirect('detail', mug_id=mug_id)

@login_required
def unassoc_coaster(request, mug_id, coaster_id):
    pass

def signup(request):
    error_message = 'L'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context =  {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)