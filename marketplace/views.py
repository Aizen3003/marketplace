from django.http import HttpResponse
from marketplace import models
from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from marketplace.forms import CustomUserCreationForm, CustomUserChangeForm

def towar_list(request):
    spisak = models.Towar.objects.all()
    otwet = render(request, "osnowa.html", {"spisak": spisak})
    return otwet

def towar(request, id):
    towarcik = models.Towar.objects.get(id=id)
    otwet = render(request, "products.html", {"towarcik": towarcik})
    return otwet

@login_required
def cart(request):
    polso = request.user
    towari_polso = models.Korsin_towari.objects.filter(korsin=polso.korsinka)
    otwet = render(request, "cart.html", {'towari_polso': towari_polso})
    return otwet

def login_polso(request):
    if request.method == "GET":
        otwet = render(request, "login.html")
        return otwet
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        prowerka = authenticate(request, username=username, password=password)
        if prowerka == None:
            otwet = render(request, "login.html")
            return otwet
        else:
            login(request, prowerka)
            otwet = redirect("towar_list")
            return otwet

def logout_polso(request):
    logout(request)
    otwet = redirect("towar_list")
    return otwet

def dobaw_towar(request):
    idtowara = int(request.POST["idtowara"])
    towarchihe = models.Towar.objects.get(id=idtowara)
    request.user.korsinka.towari.add(towarchihe)
    towarchihe.nalichie -= 1
    towarchihe.save()
    otwet = redirect('cart')
    return otwet

def regist(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            models.Korsin.objects.create(pols = user)
            login(request, user)
            otwet = redirect("towar_list")
            return otwet
        else:
            return render(request, 'regist.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'regist.html', {'form': form})
    
def corect(request):
    if request.method == "GET":
        form = CustomUserChangeForm(instance=request.user)
        otwet = render(request, "corect.html", {'form': form})
        return otwet
    elif request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            otwet = redirect('towar_list')
            return otwet
        else:
            otwet = render(request, "corect.html", {'form': form})
            return otwet
    
def delete(request):
    towarischko = int(request.POST["idtowara"])
    towarchik = models.Towar.objects.get(id=towarischko)
    deletos = models.Korsin_towari.objects.get(korsin=request.user.korsinka, towar=towarchik)
    towarchik.nalichie += deletos.kolich
    towarchik.save()
    request.user.korsinka.towari.remove(towarchik)
    otwet = redirect("cart")
    return otwet

def plus(request):
    towarischko = int(request.POST["idtowara"])
    towarchik = models.Towar.objects.get(id=towarischko)
    korsinnij_towar = models.Korsin_towari.objects.get(towar=towarchik, korsin=request.user.korsinka)
    if towarchik.nalichie >= 1:
        korsinnij_towar.kolich += 1
        towarchik.nalichie -= 1
        korsinnij_towar.save()
        towarchik.save()
    else:
        print("Недостаточно товара")
    otwet = redirect("cart")
    return otwet

def minus(request):
    towarischko = int(request.POST["idtowara"])
    towarchik = models.Towar.objects.get(id=towarischko)
    korsinnij_towar = models.Korsin_towari.objects.get(towar=towarchik, korsin=request.user.korsinka)
    korsinnij_towar.kolich -= 1
    towarchik.nalichie += 1
    korsinnij_towar.save()
    towarchik.save()
    if korsinnij_towar.kolich <= 0:
        request.user.korsinka.towari.remove(towarchik)
    otwet = redirect("cart")
    return otwet
