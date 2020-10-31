from django.shortcuts import render
from .models import Insumos
from .models import ImagenGaleria
from .models import ImagenSlider
from .models import QuienesSomos
from django.contrib.auth.models import User



from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    imagenes_slider = ImagenSlider.objects.all()
    return render(request,'core/Inicio.html',{'lista_imagenes_slider':imagenes_slider})

def galeria(request):
    imagenes = ImagenGaleria.objects.all()
    return render(request,'core/Galeria.html',{'lista_imagenes':imagenes})

def ingresar(request):
    imagenes_slider = ImagenSlider.objects.all()
    if request.POST:
        usuario = request.POST.get("Usuario")
        clave = request.POST.get("Pass")
        us = authenticate(request, username=usuario,password=clave)
        if us is not None and us.is_active:
            login(request, us)
           
            return render(request,'core/Inicio.html',{'user':us,'lista_imagenes_slider':imagenes_slider})
        else:
            return render(request,'core/Ingresar.html',{'msg':'Usuario/Contraseña incorrectos.'})
    return render(request,'core/Ingresar.html')

def logout_sesion(request):
    imagenes_slider = ImagenSlider.objects.all()
    logout(request)
    return render(request,'core/Inicio.html',{'lista_imagenes_slider':imagenes_slider})

@login_required(login_url='/ingresar/')
@permission_required('CasoSemestral.change_insumos',login_url='/ingresar/')
@permission_required('CasoSemestral.view_insumos',login_url='/ingresar/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("nombreproducto")
        precio = request.POST.get("valorproducto")
        stock = request.POST.get("stockproducto")
        descripcion = request.POST.get("descripcion")
        try:
            insumo =Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.stock = stock
            insumo.descripcion = descripcion
            insumo.save()
            msg ='Insumo Modificado'
        except:
            msg = 'No Modifico Insumo'
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_insumos.html',{'insumos':insumos,'msg':msg})
    
        




@login_required(login_url='/ingresar/')
@permission_required('CasoSemestral.view_insumos',login_url='/ingresar/')
def modificar_vista(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'core/insumos_mod.html',{'insumo':insumo})
    except:
        msg = "No Existe Insumo"
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_insumos.html',{'insumos':insumos,'msg':msg})



@login_required(login_url='/ingresar/')
@permission_required('CasoSemestral.delete_insumos',login_url='/ingresar/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg ="Insumo Eliminado"
    except:
        msg="No Elimino Insumo"
    insumos = Insumos.objects.all()
    return render(request,'core/Admin_insumos.html',{'insumos':insumos,'msg':msg})

@login_required(login_url='/ingresar/')
@permission_required('CasoSemestral.view_insumos',login_url='/ingresar/')
def admin_insumos(request):
  insumos = Insumos.objects.all()
  return render(request,'core/Admin_insumos.html',{'insumos':insumos})

@login_required(login_url='/ingresar/')
@permission_required('CasoSemestral.change_insumos',login_url='/ingresar/')
@permission_required('CasoSemestral.add_insumos',login_url='/ingresar/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("nombreproducto")
        precio = request.POST.get("valorproducto")
        stock = request.POST.get("stockproducto")
        descripcion = request.POST.get("descripcion")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion
        )

        insumo.save()
        return render(request,'core/Insumos.html',{'msg':'insumo grabado'})

    return render(request,'core/Insumos.html')




def quienes(request):
    quienes = QuienesSomos.objects.all()
    return render(request,'core/QuieneSomos.html',{'quienessomos':quienes})
    

def registro(request):

    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        usuario = request.POST.get("nomusua")
        password = request.POST.get("contrusua")

        try:
            u = User.objects.get(username=usuario)
            return render(request,'core/Registro.html',{'msg':'Usuario existente'})
        except:            
            u = User()
            u.username = usuario
            u.first_name = nombre
            u.last_name = apellido
            u.email = email
            u.set_password(password)
            u.save()

            us = authenticate(request, username=usuario,password=password)
            login(request,us)
            return render(request,'core/Registro.html',{'msg':'Usuario creado'})
    return render(request,'core/Registro.html')

def ubicacion(request):
    return render(request,'core/Ubicacion.html')