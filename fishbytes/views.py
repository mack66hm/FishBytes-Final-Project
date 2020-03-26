from django.shortcuts import render, redirect, get_object_or_404
from .models import Lake, Fish, Regulation


# Create your views here.
def homepage(request):
    lakes = Lake.objects.all()
    return render(request, 'base.html', {'lakes': lakes, })

def lake_detail(request, pk):
    lake = Lake.objects.get(pk=pk)
    fishes = lake.fish_in_lake.all()
    return render(request, 'core/lakedetail.html', {'lake': lake, 'fishes': fishes, })

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    return render(request, "core/fish_detail.html", {'fish': fish, 'pk': pk})
