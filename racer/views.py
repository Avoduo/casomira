from django.http import HttpResponse
from django.template import loader
from .models import Racer, Zavod

from django.shortcuts import render
from .forms import PersonForm

def racer(request):
    template = loader.get_template('home_racer.html')
    return HttpResponse(template.render())

def allracer(request):
    myracers = Racer.objects.all().values()
    template = loader.get_template('all-racer.html')
    context = {
        'myracers': myracers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myracer = Racer.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myracer': myracer,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def allzavod(request):
    zavod = Zavod.objects.all().values()
    template = loader.get_template('all-zavod.html')
    context = {
        'zavod': zavod,
    }
    return HttpResponse(template.render(context, request))

def details_zavod(request, id):
    zavod = Zavod.objects.get(id=id)
    template = loader.get_template('zavod.html')
    context = {
        'zavod': zavod,
    }
    return HttpResponse(template.render(context, request))

def prihlaska(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    return render(request, 'prihlaska.html', {'form': form})

def policy(request):
  template = loader.get_template('private-policy.html')
  return HttpResponse(template.render())