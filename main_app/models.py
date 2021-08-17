from django.db import models
from django.urls import reverse

max_length=100

# Create your models here.

class Mug(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    # in_use = models.BooleanField(default=True)

    def __string__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"mug_id": self.id})
    