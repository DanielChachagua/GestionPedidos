from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Pedidos.models import LineaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Carro.carro import Carro
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url='/autenticacion/loguear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.username)
    messages.success(request,'El pedido se ha  creado correctamente')
    return redirect('Home')

def enviar_mail(**kwargs):
    asunto='Gracias por el Pedido'
    mensaje=render_to_string('Emails/pedido.html',{
        'pedido':kwargs.get('pedido'),
        'lineas_pedido':kwargs.get('lineas_pedido'),
        'nombre_usuario':kwargs.get('nombre_usuario')
    })
    mensaje_texto=strip_tags(mensaje)
    from_email='danychelo92@gmail.com'
    #to=kwargs.get('email_usuario')
    to='danielmchachagua@gmail.com'
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)


    