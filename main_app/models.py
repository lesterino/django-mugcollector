from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

DRINK_TYPES = (
    ('C', 'Coffee'),
    ('T', 'Tea'),
    ('S', 'Soup'),
    ('O', 'Other')
)

class Coaster(models.Model):
    color = models.CharField(max_length=50)
    shape = models.CharField(max_length=50)

    def __str__(self):
        return self.shape
    
    def get_absolute_url(self):
        return reverse("coasters_detail", kwargs={"pk": self.id})
    

class Mug(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    in_use = models.BooleanField(default=False)
    coasters = models.ManyToManyField(Coaster)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"mug_id": self.id})

class Drink(models.Model):
    type = models.CharField(
        max_length=1,
        choices=DRINK_TYPES,
        default=DRINK_TYPES[0][0]
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    mug = models.ForeignKey(Mug, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"

    