from django.shortcuts import render
from .models import Lakes

# Create your views here.
def homepage(request):
    return render(request, 'base.html')