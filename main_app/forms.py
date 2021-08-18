from django.forms import ModelForm
from .models import Drink

class DrinkForm(ModelForm):
  class Meta:
    model = Drink
    fields = ['type', 'name', 'description']
    # fields = '__all__'