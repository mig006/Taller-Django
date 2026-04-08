from django.shortcuts import render, get_object_or_404, redirect
from .models import Cancion
from .forms import CancionForm


def cancion_lista(request):
    canciones = Cancion.objects.all()
    return render(request, 'canciones/lista.html', {'canciones': canciones})


def cancion_detalle(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, 'canciones/detalle.html', {'cancion': cancion})


def cancion_crear(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cancion_lista')
    else:
        form = CancionForm()
    return render(request, 'canciones/form.html', {'form': form, 'titulo_pagina': 'Agregar Canción'})


def cancion_editar(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('cancion_lista')
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'canciones/form.html', {'form': form, 'titulo_pagina': 'Editar Canción'})


def cancion_eliminar(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == 'POST':
        cancion.delete()
        return redirect('cancion_lista')
    return render(request, 'canciones/eliminar.html', {'cancion': cancion})
