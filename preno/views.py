from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    categorias = Categoria.objects.all()
    cursos = Curso.objects.get(nombre="General")
    context = {
        'categorias': categorias,
        'cursos': cursos,
        'cat_len': categorias.count(),

    }
    return render(request, 'preno/index.html', context)

def curso(request, curso):
    categorias = Categoria.objects.all()
    cursos = Curso.objects.get(nombre=curso)
    context = {
        'categorias': categorias,
        'cursos': cursos,
        'cat_len': categorias.count(),
    }
    return render(request, 'preno/index.html', context)