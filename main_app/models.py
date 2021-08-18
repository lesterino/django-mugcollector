from django.db import models
from django.urls import reverse

# Create your models here.

DRINK_TYPES = (
    ('C', 'Coffee'),
    ('T', 'Tea'),
    ('S', 'Soup'),
    ('O', 'Other')
)

class Mug(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    in_use = models.BooleanField(default=False)

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

    mug = models.ForeignKey(Mug, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()}"

    