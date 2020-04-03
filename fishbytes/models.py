from django.db import models
from django.utils.text import slugify
from PIL import Image
from  users.models import User
from django.http import HttpRequest
from mapbox_location_field.models import LocationField



# Create your models here.
class Lake(models.Model):
    name = models.CharField(max_length=100)
    fish_in_lake = models.ManyToManyField('Fish', related_name='lakes')
    food_safe = models.CharField(max_length=50)
    location = LocationField(map_attrs={'center': [0,0]}, null=True, blank=True)
    slug = models.SlugField(null = True, unique = True)
    lake_tag = models.ForeignKey("Tag", on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(default='default.png', upload_to='lake/')
    def __str__(self):
        return f'Lake: {self.name}'


class Fish(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    season = models.CharField(max_length=100, null=True, blank=True)
    citation = models.CharField(max_length=100, null=True, blank=True)
    record = models.CharField(max_length =100, null=True, blank=True)
    identifiers = models.TextField(max_length=550, null=True, default=None)
    regulations = models.ForeignKey(to='Regulation', blank=True, null=True, on_delete=models.DO_NOTHING)
    slug = models.SlugField(null = True, unique = True)
    img = models.ImageField(upload_to='fish/')
    fish_tag = models.ForeignKey("Tag", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Fish: {self.name}, {self.season}, {self.citation}, {self.identifiers}'

class Regulation(models.Model):
    size_min = models.CharField(max_length=200, null=True, blank=True)
    size_max = models.CharField(max_length=200, null=True, blank=True)
    weight_min = models.CharField(max_length=200, null=True, blank=True)
    weight_max = models.CharField(max_length=200, null=True, blank=True)
    daily_total =  models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Size Limit: {self.size_min}, {self.size_max}, {self.weight_min}, {self.weight_max}, Daily Limit: {self.daily_total}'

class Catch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    fish = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    lake = models.ForeignKey(Lake, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(null=False, unique=True, default=slugify(name))
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Question(models.Model):
    body = models.CharField(max_length = 500)
    pos = models.CharField(max_length = 5, blank=True, null=True)
    yesPos = models.CharField(max_length = 5, blank=True, null=True)
    noPos = models.CharField(max_length = 5, blank=True, null=True)
    def __str__(self):
        return f"{self.pos}: {self.body}"