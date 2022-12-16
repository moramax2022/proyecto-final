from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")


from ejemplo.models import Alumnos
Alumnos(nombre="Nicolás Rodríguez", curso="1CB-2", numero_matricula=100).save()
Alumnos(nombre="Ana García ", curso="1CB-2", numero_matricula=200).save()
Alumnos(nombre="Guillermo Russo", curso="1CB-3", numero_matricula=300).save()
Alumnos(nombre="Natalia Brum", curso="1CB-3", numero_matricula=400).save()
print("Se cargo con éxito los alumnos")