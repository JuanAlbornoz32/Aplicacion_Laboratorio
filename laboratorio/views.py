from django.shortcuts import render, redirect
from .models import Laboratorio
from .forms import Laboratorioform

# Create your views here.

def mostrar_view(request):
    laboratorios = Laboratorio.objects.all()
    context = {'laboratorios': laboratorios }
    return render(request, 'laboratorios.html', context)

def insertar_view(request):
    if request.method == 'POST':
        form = Laboratorioform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/laboratorios/')
    form = Laboratorioform()
    context = {'form':form}
    return render(request, 'index.html', context)

def editar_view(request,pk):
    if request.method == 'POST':
        form = Laboratorioform(request.POST)
        print(request.POST)
        if form.is_valid():
            laboratorio = Laboratorio.objects.get(id=pk)
            laboratorio.nombre = request.POST['nombre']
            laboratorio.ciudad = request.POST['ciudad']
            laboratorio.pais = request.POST['pais']
            laboratorio.save()
            return redirect('/laboratorios/')
    laboratorio = Laboratorio.objects.get(id=pk)
    form = Laboratorioform(instance=laboratorio)
    context = {'form':form, 'laboratiorio':laboratorio} 
    return render(request, 'editar.html',context)

def eliminar_view(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        laboratorio.delete()
        return redirect('/laboratorios/')
    context={'laboratorio': laboratorio}
    return render(request, 'eliminar.html', context)