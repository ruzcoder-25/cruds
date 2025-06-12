from django.shortcuts import render, redirect

from .forms import CarForm
from .models import Car


def car_list(request):
    car = Car.objects.all()
    context = {
        'car':car,
    }
    return render(request,'car/car_list.html',context)


def create_car(request):
    if request.method=='POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car-list')
    else:
        form = CarForm()

    return render(request,'car/create_car.html',{'form':form,})

def detail_car(request,pk):
    car = Car.objects.filter(pk=pk).first()
    context = {
        'car':car,
    }
    return render(request,'car/detail_car.html',context)


def update_car(request,pk):
    car = Car.objects.filter(pk=pk).first()
    if request.method=='POST':
        form = CarForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('car-list')
    else:
        form = CarForm(instance=car)
    return render(request,'car/update_car.html',{'form':form,})


def delete_car(request,pk):
    car = Car.objects.filter(pk=pk).first()
    if request.method=='POST':
        car.delete()
        return redirect('car-list')
    return render(request,'car/delete_car.html',{'car':car,})

