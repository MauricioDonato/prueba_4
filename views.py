from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.shortcuts import render
from pasteleria.models import Cliente, Comuna, Producto
from django.utils import timezone
from django.urls import reverse
import re
import sys
from itertools import cycle
# Create your views here.

def index(request):

    return render(request, 'pasteleria/index.html',)

def frm_registrar_cli(request):
    comuna = Comuna.objects.all()
    carrito = {'comuna':comuna}
    return render(request, 'pasteleria/frm_registrar_cli.html', carrito,)

def registrar_cliente(request):
    error = 'Error en el ingreso del'
    v_error = False
    primer_erro = False 
    rut_c = request.POST['rut']
    rut_c = rut_c.replace(' ','')
    rut_c = rut_c.replace('.','')
    rut_c = rut_c.replace('.','')
    rut_c = rut_c.replace('-','')
    
    nombre = request.POST['nombre']
    nombre = nombre.replace(' ','')
    apellido = request.POST['apellido'] 
    apellido = apellido.replace(' ','')
    fecha = request.POST['Fecha_nacimiento']  
    dirrecion = request.POST['dirrecion']
    comuna = request.POST['comuna']  
    correo= request.POST['correo']    
    correo = correo.replace(' ','')
    contrasena= request.POST['contrasena'] 
    contrasena= nombre.replace(' ','')   
    validar_contrasena= request.POST['validar_contrasena']    
    cantidad = len(rut_c)

    if request.POST['contrasena'] != request.POST['validar_contrasena']:
        return HttpResponse('las contraseñas deben ser iguales')
    if(fecha =="" or apellido =="" or correo =="" or nombre =="" or contrasena =="" or rut_c =="" or dirrecion=="" or comuna ==""):
        return render(request, 'pasteleria/error_ingreso.html')
    if cantidad < 8:
        return render(request, 'pasteleria/error_ingreso.html')
    if cantidad > 10:
        return render(request, 'pasteleria/error_ingreso.html')
    aux = rut_c[:-1]
    dv = rut_c[-1:]
 
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
 
    if str(res) == dv:
        v_error = True
    elif dv=="K" and res==10:
        v_error = True
    else:
        v_error = False
    if v_error == False:
        return render(request,'pasteleria/error_rut.html')
    com = Comuna.objects.get(id=comuna)
    

    cliente =Cliente(rut= rut_c, nombre_cli=nombre, apellido_cli=apellido, fecha_nac=fecha, correo=correo, direccion=dirrecion, comuna=com, contrasena=contrasena, contrasena_val=validar_contrasena)
    cliente.save()
  
 
    return HttpResponseRedirect(reverse('pasteleria:cliente_regitrado'))
def cliente_regitrado(request):
    return render(request,'pasteleria/cliente_regitrado.html')

def frm_buscar_cliente(request):
    return render(request,'pasteleria/frm_buscar_cliente.html')
def buscar_y_mostrar_cliente(request):
    rut_b = request.POST['rut_b']
    rut_b = rut_b.replace('.','')
    rut_b = rut_b.replace('.','')
    rut_b = rut_b.replace('-','')

    listado =  Cliente.objects.filter(rut__startswith=rut_b)   
    
    carrito = {'listado':listado}
    return render(request, 'pasteleria/mostrar_cliente.html',carrito)
   
def eliminar_cliente(request):
    eliminador = Cliente.objects.get(id= request.POST['id_e'])
    eliminar_mostrar = {'eliminador':eliminador}
    return render(request, 'pasteleria/eliminar_cliente.html',eliminar_mostrar)
def eliminador_cliente(request):
    elim =  Cliente.objects.get(id= request.POST['id_eliminado'])
    elim.delete()
    return render(request, 'pasteleria/cliente_eliminado.html',)
def editar_cliente(request):
    editar =  Cliente.objects.get(id= request.POST['id_d'])
    comuna = Comuna.objects.all()
    editar_mostrar ={'editar': editar,'comuna':comuna}
    
      
    return render(request, 'pasteleria/editar_cliente.html',editar_mostrar, )
def editador_cliente(request):
    e = Cliente.objects.get(id= request.POST['id_editor'])
    rut_c = request.POST['rut_editor']
    rut_c = rut_c.replace(' ','')
    nombre = request.POST['nombre_editor']
    nombre = nombre.replace(' ','')
    apellido = request.POST['apellido_editor'] 
    apellido = apellido.replace(' ','')
    fecha = request.POST['Fecha_nacimiento_editor']  
    correo= request.POST['correo_editor']    
    correo = correo.replace(' ','')
    dirrecion = request.POST['dirrecion']
    comuna = request.POST['comuna'] 
    contrasena= request.POST['contrasena_editor'] 
    contrasena = contrasena.replace(' ','')   
    validar_contrasena= request.POST['validar_contrasena_editor']
    if request.POST['contrasena_editor'] != request.POST['validar_contrasena_editor']:
        return HttpResponse('las contraseñas deben ser iguales')
    if(fecha =="" or apellido =="" or correo =="" or nombre =="" or contrasena =="" or rut_c ==""):
        return render(request, 'pasteleria/error_ingreso.html')
    if len(request.POST['rut_editor']) < 8 and len(request.POST['rut_editar']) < 10:
        return render(request, 'pasteleria/error_ingreso.html')
    aux = rut_c[:-1]
    dv = rut_c[-1:]
 
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
 
    if str(res) == dv:
        v_error = True
    elif dv=="K" and res==10:
        v_error = True
    else:
        v_error = False
    if v_error == False:
        return render(request,'pasteleria/error_rut.html')
    com = Comuna.objects.get(id=comuna)
    
    e.rut = rut_c
    e.nombre_cli = nombre
    e.apellido_cli = apellido
    e.fecha_nac = fecha
    e.correo = correo
    e.direccion = dirrecion
    e.comuna = com
    e.contrasena = contrasena
    e.contrasena_val = validar_contrasena

    e.save()
    return render(request, 'pasteleria/editar_c.html',)   

def frm_comuna(request):
    return render(request, 'pasteleria/frm_comuna.html', )
def registrar_comuna(request):
    nombre_com = request.POST['nombre_comuna']
    nombre_com = nombre_com.replace(' ','')
    if(nombre_com ==""):
        return render(request, 'pasteleria/error_ingreso.html',)  
    comuna = Comuna(nombre_c=nombre_com)
    comuna.save()
    return render(request, 'pasteleria/comuna_registrado.html',) 

def frm_buscar_comuna(request):
    return render(request,'pasteleria/frm_buscar_comuna.html')
def buscar_y_mostrar_comuna(request):
    nombre_c = request.POST['nombre_buscar']

    listado =  Comuna.objects.filter(nombre_c__startswith=nombre_c)   
    
    carrito = {'listado':listado} 
    return render(request, 'pasteleria/mostrar_comuna.html',carrito)
def eliminar_comuna(request):
    eliminador = Comuna.objects.get(id= request.POST['id_e'])
    eliminar_mostrar = {'eliminador':eliminador}
    return render(request, 'pasteleria/eliminar_comuna.html',eliminar_mostrar)
def eliminador_comuna(request):
    elim =  Comuna.objects.get(id= request.POST['id_eliminado'])
    elim.delete()
    return render(request, 'pasteleria/comuna_eliminado.html',)
def editar_comuna(request):
    comuna =  Comuna.objects.get(id= request.POST['id_d'])
    editar_mostrar ={'comuna':comuna}  
    return render(request, 'pasteleria/editar_comuna.html',editar_mostrar, )

def editador_comuna(request):
    e = Comuna.objects.get(id= request.POST['id_editor'])
    nombre_com = request.POST['nombre_editor']
    nombre_com = nombre_com.replace(' ','')
    if(nombre_com ==""):
        return render(request, 'pasteleria/error_ingreso.html',)  
    e.nombre_c = nombre_com
    e.save()
    return render(request, 'pasteleria/comuna_registrado.html',) 

def frm_producto(request):
    return render(request, 'pasteleria/frm_producto.html', )
def registrar_producto(request):
    nombre_com = request.POST['nombre_producto']

    precio = request.POST['precio_producto']
    if(nombre_com =="" or precio == 0 ):
        return render(request, 'pasteleria/error_ingreso.html',)  
    p = Producto(nombre_pro=nombre_com, precio_pro=precio)
    p.save()
    return render(request, 'pasteleria/producto_registrado.html',) 
def frm_buscar_producto(request):
    return render(request,'pasteleria/frm_buscar_producto.html')
def buscar_y_mostrar_producto(request):
    nombre_p = request.POST['nombre_buscar']

    listado =  Producto.objects.filter(nombre_pro__startswith=nombre_p)   
    
    carrito = {'listado':listado} 
    return render(request, 'pasteleria/mostrar_producto.html',carrito)
def eliminar_producto(request):
    eliminador = Producto.objects.get(id= request.POST['id_e'])
    eliminar_mostrar = {'eliminador':eliminador}
    return render(request, 'pasteleria/eliminar_producto.html',eliminar_mostrar)    
def eliminador_producto(request):
    elim =  Producto.objects.get(id= request.POST['id_eliminado'])
    elim.delete()
    return render(request, 'pasteleria/producto_eliminado.html',)
def editar_producto(request):
    producto =  Producto.objects.get(id= request.POST['id_d'])
    editar_mostrar ={'producto':producto}  
    return render(request, 'pasteleria/editar_producto.html',editar_mostrar, )
def editador_producto(request):
    e = Producto.objects.get(id= request.POST['id_editor'])
    nombre_com = request.POST['nombre_editor']
    precio_e = request.POST['precio_editor']
    if(nombre_com =="" or precio_e ==0 ):
        return render(request, 'pasteleria/error_ingreso.html',)  
    e.nombre_c = nombre_com
    e.precio_pro = precio_e
    e.save()
    return render(request, 'pasteleria/producto_registrado.html',) 