from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Auto, Cliente
from .forms import MarcaForm, AutoForm, ClienteForm

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'marcas/lista.html', {'marcas': marcas})

def crear_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_marcas')
    return render(request, 'marcas/formulario.html', {'form': form})

def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    if form.is_valid():
        form.save()
        return redirect('lista_marcas')
    return render(request, 'marcas/formulario.html', {'form': form})

def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('lista_marcas')
    return render(request, 'marcas/confirmar_eliminar.html', {'obj': marca})


def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/lista.html', {'autos': autos})

def crear_auto(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_autos')
    return render(request, 'autos/formulario.html', {'form': form})

def editar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    form = AutoForm(request.POST or None, instance=auto)
    if form.is_valid():
        form.save()
        return redirect('lista_autos')
    return render(request, 'autos/formulario.html', {'form': form})

def eliminar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_autos')
    return render(request, 'autos/confirmar_eliminar.html', {'obj': auto})


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/formulario.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/formulario.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/confirmar_eliminar.html', {'obj': cliente})

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')



