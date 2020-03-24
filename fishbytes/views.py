from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def lakedetail(request, pk):
    lake = Lakes.objects.get(pk=pk)
    fish = lake.fish_in_lake
    return render(request, 'core/lakedetail.html', {'lake': lake, 'fish': fish, })