from django.http import HttpResponse
from web_MVT.models import *
from django.template import Template, Context, loader
from django.shortcuts import render
from web_MVT.forms import *

# Create your views here.
def index(request):
   return render(request,"web_MVT/categoria.html")

def productViews(request):
   if request.method == "POST":
      myformulario= productForm(request.POST)
      if myformulario.is_valid():
         
         infom=myformulario.cleaned_data

         products= product(code = infom["code"],name = infom["name"],description = infom["description"],
         category = infom["category"], price = infom["price"])
         products.save()


   formularios= productForm() 
   return render(request,"web_MVT/producto.html",{"formulario": formularios})

def registerViews(request):
   if request.method == "POST":
      myformulario= registerForm(request.POST)
      if myformulario.is_valid():
         
         infom=myformulario.cleaned_data

         registers= register(firtname = infom["firtname"],lastname= infom["lastname"],
         phone = infom["phone"],email= infom["email"],password = infom["password"])
         registers.save()


   formularios= registerForm() 
   return render(request,"web_MVT/registro.html",{"formulario": formularios})   

def categoryViews(request):
   if request.method == "POST":
      myformulario= categoriForm(request.POST)
      if myformulario.is_valid():
         
         infom=myformulario.cleaned_data
         categorys= category(name=infom["name"],description=infom["description"])
         categorys.save()
   
   formularios= categoriForm()   
   return render(request,"web_MVT/categoria.html",{"formulario": formularios})         


def searchItem(request):

   if request.GET:
      nombre_producto = request.GET.get("buscar_producto", "")
      if nombre_producto == "":
         resultprod = []
      else:
         resultprod = product.objects.filter(name__icontains=nombre_producto)
      return render(request, "web_MVT/search.html", {"listado_producto": resultprod})

   return render(request, "web_MVT/search.html", {"listado_producto": []})

 