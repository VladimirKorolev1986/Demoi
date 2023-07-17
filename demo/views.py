import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
import random

from demo.models import Car, Person


def index(request):
    return HttpResponse("Hello my Django")


def time(request):
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Time = {current_time}')


def hello(request):
    context = {
        'test': 5,
        'data': [1, 5, 8],
        'val': 'hello',
    }
    return render(request, 'demo.html', context)


def sum(request, a, b):
    result = a + b
    return HttpResponse(f"Summa = {result}")


CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(5)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)


def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'M3']),
        color=random.choice(['C1', 'C2', 'C3']))
    car.save()
    return HttpResponse(f'Всё получилось! Новая машина: {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.filter(brand__contains='2')
    cars = [f'{c.id}, {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person(name='P', car=car).save()
    return HttpResponse('Всё получилось')

def list_person(request):
    people_objects = Person.objects.all()
    people = [f'{p.name}, {p.car}' for p in people_objects]
    return HttpResponse('<br>'.join(people))

