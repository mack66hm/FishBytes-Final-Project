from django.shortcuts import render, redirect, get_object_or_404
from .models import Lakes, Fish, Regulations


# Create your views here.
def homepage(request):
    lakes = Lakes.objects.all()
    return render(request, 'base.html', {'lakes': lakes, })

def lakedetail(request, pk):
    lake = Lakes.objects.get(pk=pk)
    fishes = lake.fish_in_lake
    return render(request, 'core/lakedetail.html', {'lake': lake, 'fishes': fishes, })

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    return render(request, "core/fish_detail.html", {'fish': fish, 'pk': pk})
