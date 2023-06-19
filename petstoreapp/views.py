from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto
from .forms import ProductoForm, RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'sobre nosotros.html')

def galeria(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'galeria.html', data)

def formulario(request):
    return render(request, 'formulario.html')

def api(request):
    return render(request, 'api.html')

@login_required
def lista_productos(request):
    producto = Producto.objects.all().order_by('codigo')
    context = {
        'producto' : producto
    }
    return render(request, 'lista-productos.html', context)

@login_required
def crear_producto(request):
    context = {
        'form': ProductoForm
    }
    if request.method=='POST':
        productos_form = ProductoForm(data=request.POST, files=request.FILES)
        if productos_form.is_valid():
            productos_form.save()
            return redirect(to="lista_productos")
        else:
            context['form'] = productos_form
    
    return render(request, 'crear-producto.html', context)

@login_required
def modificar_producto(request, id):
    productos = get_object_or_404(Producto, codigo=id)
    datos = {
        'form': ProductoForm(instance = productos)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_productos")
        datos["form"] = formulario
              
    return render(request, 'modificar-producto.html', datos)

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, codigo=id)
    producto.delete()
    return redirect(to="lista_productos") 

#Autenticación
def registro_usuario(request):
    data = {
        'form' : RegistroForm()        
    }
    if request.method=="POST":
        formulario = RegistroForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('index')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


