from django.db import models

# Create your models here.


class Pokemon(models.Model):
    identifier = models.CharField(max_length=255)
    species_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField(default=0)
    order = models.IntegerField(default=1)
    is_default = models.BooleanField(default=True)
