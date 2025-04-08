from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

def home(request):
    app1 = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': app1})

from django.contrib.auth.decorators import login_required


def home(request):
    app1 = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': app1})
