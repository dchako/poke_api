from django.db import models
from datetime import datetime

# Create your models here.
class Cards(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hp = models.PositiveIntegerField(default=0, )
    start_date = models.DateTimeField(default=datetime.now(), blank=True)
    types = models.ForeignKey('Types', related_name='types')
    expansion = models.ForeignKey('Expansion', related_name='expansions')
    rarity = models.ChoiceField(
                  choices=(
                            ("COMUN", "comun"),
                            ("NO COMUN", "no comun"),
                            ("RARA", "rara")
                            ),
                  default="COMUN")
    price = models.FloatField(blank=False,max_length=99999.9,default=0.0)
    image_cards = models.URLField(blank=True)
    is_firts_edition = models.BooleanField(default=False)
    
class Types(models.Model):
    types = models.CharField(max_length=30, unique=True)

class Expansion(models.Model):
    expansion = models.CharField(max_length=30, unique=True)
