from django.db import models

# Create your models here.
class Lakes(models.Model):
    name = models.CharField(max_length=100)
    fish_in_lake = models.ForeignKey(to='Fish', on_delete=models.DO_NOTHING, related_name='fish')
    food_safe = models.CharField(max_length=50)

    def __str__(self):
        return f'Lake: {self.name}'


class Fish(models.Model):
    pass