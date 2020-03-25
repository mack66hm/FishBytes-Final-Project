from django.db import models

# Create your models here.
class Lakes(models.Model):
    name = models.CharField(max_length=100)
    fish_in_lake = models.ForeignKey(to='Fish', on_delete=models.DO_NOTHING, related_name='fish')
    food_safe = models.CharField(max_length=50)

    def __str__(self):
        return f'Lake: {self.name}'


class Fish(models.Model):
    fish_name = models.CharField(max_length=100, null=True, blank=True)
    season = models.CharField(max_length=100, null=True, blank=True)
    citation = models.CharField(max_length=100, null=True, blank=True)
    identifiers = models.CharField(max_length=350, null=True, default=None)
    found_in = models.ForeignKey(to=Lakes, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='lake')
    regulations = models.ForeignKey(to='Regulations', blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Fish: {self.fish_name}, {self.season}, {self.citation}, {self.identifiers}'

class Regulations(models.Model):
    size_min = models.CharField(max_length=200, null=True, blank=True)
    size_max = models.CharField(max_length=200, null=True, blank=True)
    weight_min = models.CharField(max_length=200, null=True, blank=True)
    weight_max = models.CharField(max_length=200, null=True, blank=True)
    daily_total =  models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Size Limit: {self.size_min}, {self.size_max}, {self.weight_min}, {self.weight_max}, Daily Limit: {self.daily_total}'

    