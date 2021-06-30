from django.shortcuts import redirect ,render
from .models import Ropa,Categoria
from .forms import ropaForm

# Create your views here.

def home (request):
    return render (request , "core/html")

def ropa_tienda(request):
    data = {"list": Ropa.objects.all().order_by('idRopa')}
    return render (request, "core/ropa_tienda.html",data)

def ropa_ficha(request, id):
    ropa = Ropa.objects.get(idRopa=id)
    data = {"Prenda": ropa}
    return render (request,"core/ropa_ficha.html",data)

def ropa(request, action, id):
    
    data={"mesg": "", "form": ropaForm, "action":action, "id":id}
   
    if request.method == "POST":
        form = ropaForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
                data ["mesg"] = "Ropa ingresada correctamente"
            except:
                data ["mesg"] = "No se puede ingresar un codigo usado"
    elif action == 'upd':
        objeto = Ropa.objects.get(idRopa=id)
        if request.method =="POST":
            form=ropaForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "Ropa Actualizada correctamente"
        data["form"] = ropaForm(instance=objeto)
    
    elif action == 'del':
        try:
            Ropa.objects.get(idRopa=id).delete()
            data["mesg"] = "Ropa Eliminada correctamente"
            return redirect(ropa, action='ins', id='-1')
        except:
            data["mesg"]= "Esta Ropa Ya estaba eliminada"
    
    data["list"] = Ropa.objects.all().order_by('idRopa')
    return render (request,"core/ropa.html")


    

def poblar_bd(request):
    Ropa.objects.all().delete()
    Ropa.objects.create(idRopa="AA0011", marcaRopa='JMarket', precioRopa=9900, descripcionRopa="Pantalón mezclilla de hombre", imagenRopa="images/moda2.jpg", categoriaRopa=Categoria.objects.get(idCategoria=2))
    Ropa.objects.create(idRopa="AA0022", marcaRopa='JMarket', precioRopa=29900, descripcionRopa="Chaqueta Nylon mujer", imagenRopa="images/moda3.jpg", categoriaRopa=Categoria.objects.get(idCategoria=2))
    Ropa.objects.create(idRopa="AA0033", marcaRopa='Fashion J', precioRopa=7900, descripcionRopa="Polera algodón mujer", imagenRopa="images/moda4.jpg", categoriaRopa=Categoria.objects.get(idCategoria=2))
    Ropa.objects.create(idRopa="AA0044", marcaRopa='Fashion J', precioRopa=4990, descripcionRopa="Polera corazón mujer", imagenRopa="images/moda5.jpg", categoriaRopa=Categoria.objects.get(idCategoria=2))
    return redirect(ropa, action='ins', id = '-1')
