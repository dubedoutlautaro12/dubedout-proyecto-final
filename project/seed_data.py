from ejemplo.models import Familiar, Vehiculo
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Vehiculo(dueno= 'Lautaro', tipo= 'Auto', patente='aa 109 aa').save() 
print("Se cargo con éxito los usuarios de pruebas")

