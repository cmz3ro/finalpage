from django.shortcuts import render
from main_app.models import Treni_led,Treni_rapishot,Treni_dorojka,Treni_ofp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_app1(request):
    args = {}
    args['first_pages'] = 'active'
    return render(request, 'index.html')


def net_gh(request):
    return render(request, 'new.html')

def treni(request):
    args={}
    args['led'] = Treni_led.objects.all()
    args['rapishot'] = Treni_rapishot.objects.all()
    args['dorojka'] = Treni_dorojka.objects.all()
    args['ofp'] = Treni_ofp.objects.all()
    return render(request, 'treni.html',args)

def rapid(request):
    return render(request, 'sbori.html')

def sbori1(request):
    return render(request, 'sbori1.html')

def tumba(request):
    return render(request, 'tumba.html')

def commanda(request):
    args = {}
    args['first_pages'] = 'active'
    return render(request, 'commanda.html')
      
def vorota(request):
    return render(request, 'vorota.html')

def sopernik(request):
    return render(request, 'sopernik.html')

def produkiay(request):
    args = {}
    args['first_pages'] = 'active'
    return render(request, 'produkiay.html')