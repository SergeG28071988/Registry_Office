from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Marriage
from .models import Divorce
from .marriage_form import MarriageForm

# Create your views here.


def index(request):
     context = {
         'title': 'Главная страница сайта' 
         }
     return render(request, 'base/index.html', context)


def marriage_list(request):
    marriages = Marriage.objects.order_by('-id')
    context = {'title': 'Браки', 'marriages': marriages} 
    return render(request, 'base/marriage_list.html', context)


def add_marriage(request):
    error = ''
    if request.method == 'POST':
        form = MarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marriage_list')
        else:
            error = "Форма была не верной"
    
    form = MarriageForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'base/add_marriage.html', context)


def marriage_detail(request, pk):
    marriage = get_object_or_404(Marriage, pk=pk)
    return render(request, 'base/marriage_detail.html', {'marriage': marriage})


def delete_marriage(request, pk):
    marriage = get_object_or_404(Marriage, pk=pk)
    marriage.delete()
    return redirect('index')

def edit_marriage(request, pk):
    marriage = get_object_or_404(Marriage, pk=pk)

    if request.method == 'POST':
        form = MarriageForm(request.POST, instance=marriage)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MarriageForm(instance=marriage)

    return render(request, 'base/edit_marriage.html', {'form': form})


def divorce_list(request):
    divorces = Divorce.objects.order_by('-id')
    context = {'title': 'Разводы',  'divorces': divorces} 
    return render(request, 'base/divorce_list.html', context)


