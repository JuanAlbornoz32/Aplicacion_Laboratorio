from django.shortcuts import render, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

# Create your views here.

def mostrar_view(request):
    laboratorios = Laboratorio.objects.all()
    num_visitas = request.session.get('num_visitas', 0)
    num_visitas += 1
    request.session['num_visitas'] = num_visitas
    context = {
        'laboratorios': laboratorios,
        'num_visitas': num_visitas,
        }
    return render(request, 'mostrar.html', context)

def insertar_view(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mostrar/')
    form = LaboratorioForm()
    context = {'form':form}
    return render(request, 'insertar.html', context)

def editar_view(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    context = {'laboratorio':laboratorio} 
    return render(request, 'editar.html', context)

def actualizar_view(request, pk):
    nombre = request.POST['nombre'] 
    ciudad = request.POST['ciudad'] 
    pais = request.POST['pais'] 
    laboratorio = Laboratorio.objects.get(id=pk) 
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save() 
    return redirect('/mostrar/')

def eliminar_view(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        laboratorio.delete()
        return redirect('/mostrar/')
    context={'laboratorio': laboratorio}
    return render(request, 'eliminar.html', context)