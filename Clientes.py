from collections import deque

class Cliente:
    def __init__(self, nombre, es_vip):
        self.nombre = nombre
        self.es_vip = es_vip 

    def __str__(self):
        return f"{self.nombre} (VIP)" if self.es_vip else f"{self.nombre} (Regular)"

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







    
