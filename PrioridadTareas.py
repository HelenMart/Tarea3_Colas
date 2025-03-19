#Implementar un gestor de tareas con prioridad donde las tareas urgentes sean atendidas antes de las tareas normales.#
#Se deben manejar dos colas:
#Cola de alta prioridad (procesos críticos).
#Cola normal (procesos estándar).
#El programa debe permitir agregar tareas con diferentes niveles de prioridad y procesarlas en orden correcto.
from collections import deque

class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def  __str__(self):
        return f"Tarea: {self.nombre} | Prioridad: {self.prioridad}"

alta = deque()
media = deque()
baja = deque()
print(f"\nReordenador de tareas")
print(f"Tipos de prioridad para las tareas: ")
print(f"1. Alta")
print(f"2. Media")
print(f"3. Baja")

num = int(input(f"\nCuantas tareas desea agregar :"))
for i in range(1, num + 1): 
    Tareaactual = input(f"\nIngrese la tarea {i}: ")
    prioridad = int(input(f"Ingrese el numero de prioridad: "))

    if prioridad == 1:
     nuevaT = Tarea(Tareaactual,prioridad)
     alta.append(nuevaT)
    elif prioridad == 2:
     nuevaT = Tarea(Tareaactual,prioridad)
     media.append(nuevaT)
    elif prioridad == 3:
     nuevaT = Tarea(Tareaactual,prioridad)
     baja.append(nuevaT)
    else: 
       print(f"\nHa ingresado una tarea fuera de los limites requeridos")
    
def mostrar_cola(titulo, cola):
    print(f"\n🔹 {titulo}:")
    if not cola:
        print("   (No hay tareas)")
    else:
        for tarea in cola:
            print(f"   - {tarea}")

print(f"\nTareas Agregadas correctamentes")
print(f"\nEstas son las tareas clasificadas por prioridad:")
mostrar_cola("Prioridad ALTA", alta)
mostrar_cola("Prioridad MEDIA", media)
mostrar_cola("Prioridad BAJA", baja)