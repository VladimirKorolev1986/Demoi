import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator


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
