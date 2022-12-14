from django.shortcuts import render
from django.shortcuts import get_object_or_404
from ejemplo.forms import Buscar 
from ejemplo.models import Familiar
from ejemplo.models import Mascota
from ejemplo.models import Vehiculo
from ejemplo.forms import FamiliarForm
from ejemplo.forms import MascotaForm
from ejemplo.forms import VehiculoForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


def buscar(request):
    lista_de_nombre = ['German', 'Daniel', 'Romero', 'Alvaro']    
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_del_resultado = lista_de_nombre.index(query)
        resultado= lista_de_nombre[indice_del_resultado]
    else:
        resultado = 'NO HAY MATCH'
    return render(request, 'ejemplo/buscar.html', {'resultado': resultado})

def pagina_principal(request):
    return render (request, 'ejemplo/pagina_principal.html')

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
 


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
        




class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con ??xito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualiz?? con ??xito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})


def mostrar_mascotas(request):
  lista_mascotas = Mascota.objects.all()
  return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class BuscarMascota(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_mascota.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})


class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascotas.html'
    initial = {"nombre":"", "dueno":"", "peso":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con ??xito {form.cleaned_data.get('nombre')} la mascota de {form.cleaned_data.get('dueno')} "
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "dueno":"", "peso":""}
  
  def get (self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

 
  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid(): 
          form.save()
          msg_exito = f"se actualiz?? con ??xito la informacion de {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})



class BorrarMascota(View):
  template_name = 'ejemplo/mascotas.html'
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      mascota.delete()
      mascotas = Mascota.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascotas})

def mostrar_vehiculo(request):
    lista_vehiculos = Vehiculo.objects.all()
    return render(request, 'ejemplo/vehiculos.html', {'lista_vehiculos': lista_vehiculos})



class BuscarVehiculo(View):
    form_class= Buscar
    template_name= 'ejemplo/buscar_vehiculo.html'
    initial= {'dueno':''}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post (self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('dueno')
            lista_vehiculos = Vehiculo.object.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_vehiculos': lista_vehiculos})
        return render (request, self.template_name, {'form': form})

class AltaVehiculo(View):
    form_class = VehiculoForm
    template_name = 'ejemplo/alta_vehiculo.html'
    initial= {'dueno':'', 'tipo':'', 'patente':'', 'modelo':''}

    def get(self,request):
        form = self.form_class(initial=self.initial)
        return render (request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con ??xito el {form.cleaned_data.get('tipo')} de {form.cleaned_data.get('dueno')} "
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
        


class ActualizarVehiculo(View):
  form_class = VehiculoForm
  template_name = 'ejemplo/actualizar_vehiculo.html'
  initial = {'dueno':'', 'tipo':'', 'patente':'', 'modelo':''}
  
  def get (self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(instance=vehiculo)
      return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

 
  def post(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculo)
      if form.is_valid(): 
          form.save()
          msg_exito = f"se actualiz?? con ??xito la informacion del {form.cleaned_data.get('tipo')} de {form.cleaned_data.get('dueno')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarVehiculo(View):
  template_name = 'ejemplo/vehiculos.html'
  
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      vehiculo.delete()
      vehiculos = Vehiculo.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})


class FamiliarList(ListView):
    model = Familiar

class FamiliarCrear(CreateView):
    model=Familiar
    success_url= '/panel-familia'
    fields = ['nombre', 'direccion', 'numero_pasaporte']


class FamiliarBorrar(DeleteView):
    model= Familiar
    success_url= '/panel-familia'

class FamiliarActualizar(UpdateView):
    model = Familiar 
    success_url= '/succes_update_message'
    fields = ['nombre', 'direccion', 'numero_pasaporte']



