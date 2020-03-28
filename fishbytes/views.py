from django.shortcuts import render, redirect, get_object_or_404
from fishbytes.models import Lake, Fish, Regulation, Tag, Catch
from fishbytes.forms import CatchForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest




# Create your views here.
def homepage(request):
    lakes = Lake.objects.all()
    return render(request, 'base.html', {'lakes': lakes, })

def lake_detail(request, pk):
    lake = Lake.objects.get(pk=pk)
    fishes = Fish.objects.filter(lakes__name__contains=lake.name)
    return render(request, 'core/lake_detail.html', {'lake': lake, 'fishes': fishes, })

def fish_detail(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    lakes = fish.lakes.all()
    return render(request, "core/fish_detail.html", {'lakes': lakes, 'fish': fish, 'pk': pk})

@login_required
def profile_page(request):
    catch = Catch.objects.all()
    return render(request, 'core/profile_page.html', {'catch': catch})

@login_required
def add_catch(request):
    if request.method =='POST':
        form = CatchForm(request.POST)
        if form.is_valid():
            catch = form.save(commit=False)
            catch.save()
            return redirect('profile-page')
    else:
        form = CatchForm()
    return render(request, 'core/add_catch.html', {'form': form})

@login_required
def edit_catch(request, pk):
    catch = get_object_or_404(Catch, pk=pk)
    if request.method == 'POST':
        form = CatchForm(request.POST, instance=catch)
        catch = form.save(commit=False)
        catch.save
        return redirect('add-catch', pk=catch.pk)
    else: 
        form = CatchForm(instance=catch)
    return render(request, 'core/edit_catch.html', {'form': form}) 



