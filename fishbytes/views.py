from django.shortcuts import render, redirect, get_object_or_404
from .models import Lakes, Fish, Regulations


# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def lakedetail(request, pk):
    lake = Lakes.objects.get(pk=pk)
    fish = lake.fish_in_lake
    return render(request, 'core/lakedetail.html', {'lake': lake, 'fish': fish, })

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    return render(request, "core/fish_detail.html", 'fish':fish, 'pk': pk)