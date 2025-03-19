## Descripcion
#### 1.  Programa que me permita Implementar un gestor de tareas con prioridad donde las tareas urgentes sean atendidas antes de las tareas normales.
- Tendremos 3 colas respectivamente para las prioridades altas, medianas y bajas, dpendiendo de estas se ordenaran y se mostraran en pantalla en el orden que se deben atender.
### Clase para las tareas
```python
class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def  __str__(self):
        return f"Tarea: {self.nombre} | Prioridad: {self.prioridad}"
```

### Colas utilizadas
    from collections import deque
    alta = deque()
    media = deque()
    baja = deque()

### Asignacion de prioridades 
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

### Funcion final
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
	

#### 2.Simulación de un sistema de atención al cliente,  donde los clientes sean atendidos en orden de llegada, pero si un cliente VIP entra en la cola, debe ser atendido antes que los clientes regulares
### Clase para clientes
```python
class Cliente:
    def __init__(self, nombre, es_vip):
        self.nombre = nombre
        self.es_vip = es_vip 

    def __str__(self):
        return f"{self.nombre} (VIP)" if self.es_vip else f"{self.nombre} (Regular)"
```
### Clase de metodos basicos
```python
class Atencion:
    def __init__(self):
        self.cola = deque()

    def agregar(self, cliente):
        if cliente.es_vip:
            self.cola.appendleft(cliente)
        else:
            self.cola.append(cliente)

    def atender_cliente(self):
        if self.cola:
            return self.cola.popleft()
        else:
            return None  

    def mostrar_cola(self):
        if not self.cola:
            print("No hay clientes en la cola.")
        else:
            print("Clientes en la cola:")
            for cliente in self.cola:
                print(cliente)

```
### Agregar clientes y atender
```python
cola = Atencion()  #creando instanciia
cola.agregar(Cliente("Lucia Fernanda Santos", False))
cola.agregar(Cliente("Luis Fernando Martinez", True))
cola.agregar(Cliente("José Adolfo Maldonado", False))
cola.agregar(Cliente("Andy Esteban Mazariegos", False))
cola.agregar(Cliente("Oliver Santiago Meyers", True))
cola.agregar(Cliente("Aaron Sebastian Malen", True))

cola.mostrar_cola()

print("\nAtendiendo a los clientes:")
while True:
        cliente_atendido = cola.atender_cliente()  # llamar el método en la instancia
        if cliente_atendido:
            print(f"Atendiendo a: {cliente_atendido}")
        else:
            break

```
