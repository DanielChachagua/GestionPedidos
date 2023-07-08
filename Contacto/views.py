from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):  
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            email=EmailMessage("Mensaje desde AppDjango",
            "El usuario de nombre: {} con la direccion: {} escribe lo siguiente: \n\n{}".format(nombre,email,contenido),
            "",["danychelo92@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?no_valido")
    return render(request,'Contacto/contacto.html',{'miformulario':formulario_contacto})   
