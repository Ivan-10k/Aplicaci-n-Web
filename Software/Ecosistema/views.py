from django.shortcuts import render, redirect
from .models import Ecosistema
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def home(request):
    EcosistemasListados = Ecosistema.objects.all()
    return render(request, "gestionEco.html", {"Ecosistemas": EcosistemasListados})

def registrarEcosistema(request):
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']
    area = request.POST['txtArea']
    ubicacion = request.POST['txtUbicacion']
    descripcion = request.POST['txtDescripcion']
    
    messages.success(request, '¡Curso registrado!')
    
    ecosistema = Ecosistema.objects.create(nombre=nombre, tipo=tipo, area=area, ubicacion=ubicacion, descripcion=descripcion)
    return redirect('/')


def edicionEcosistema(request, nombre):
    ecosistema = Ecosistema.objects.get(nombre=nombre)
    return render(request, "edicionEco.html", {"ecosistema": ecosistema})



def editarEcosistema(request):
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']
    area = request.POST['txtArea']
    ubicacion = request.POST['txtUbicacion']
    descripcion = request.POST['txtDescripcion']
    
    ecosistema = Ecosistema.objects.get(nombre=nombre)
    ecosistema.tipo = tipo
    ecosistema.area = area
    ecosistema.ubicacion = ubicacion
    ecosistema.descripcion = descripcion
    ecosistema.save()
    
    messages.success(request, '¡Ecosistema actualizado!')
    
    return redirect('/')
    
def eliminarEcosistema(request, nombre):
    ecosistema = Ecosistema.objects.get(nombre=nombre)
    ecosistema.delete()
    
    messages.success(request, '¡Curso eliminado!')
    
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal después de iniciar sesión
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Te has registrado exitosamente!')
            return redirect('login')  # Redirige a la página de login después del registro
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})