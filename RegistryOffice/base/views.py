from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Marriage
from .models import Divorce
from .marriage_form import MarriageForm
from .divorce_form import DivorceForm
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
            return redirect('index')
        else:
            error = "Форма была не верной"
            return redirect('marriage_list')
    
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


def create_divorce(request):
    error = ''
    if request.method == 'POST':
        form = DivorceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('divorce_list')
        else:
            error = "Форма была не верной"
    
    form = DivorceForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'base/create_divorce.html', context)


def divorce_detail(request, pk):
    divorce = get_object_or_404(Divorce, pk=pk)
    return render(request, 'base/divorce_detail.html', {'divorce': divorce})


def delete_divorce(request, pk):
    divorce = get_object_or_404(Divorce, pk=pk)
    divorce.delete()
    return redirect('divorce_list')


def edit_divorce(request, pk):
    divorce = get_object_or_404(Divorce, pk=pk)

    if request.method == 'POST':
        form = DivorceForm(request.POST, instance=divorce)
        if form.is_valid():
            form.save()
            return redirect('divorce_list')
    else:
        form = DivorceForm(instance=divorce)

    return render(request, 'base/edit_divorce.html', {'form': form})


def about(request):
    return render(request, 'base/about.html')