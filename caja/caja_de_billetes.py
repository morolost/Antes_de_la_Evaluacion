#tenes una caja esta se le van ingresando o quitando billetes estos billetes solo pueden ser de 1,2,5,10,20,50,100,200,500,1000
#este tambien debe de tener un metodo el cual le permita agregar o realizar pagos 
from cola import Cola
cola = Cola()
"""
class Caja:
    def __init__(self,denominacion):
        self.deno = denominacion
        self.permitidas = [1,2,5,10,20,50,100,200,500,1000]
        self.cola_de_pagos = cola
        
    def agregar(self):
        b = int(input("ingrese numero del billete: "))
        for i in self.permitidas:
            if b == i:
                if b in self.deno:
                    self.deno[b] = self.deno[b] + 1
                    print(f"Billete aceptado {self.deno}")
                    
             
    def quitar(self):
        b = int(input("ingrese numero del billete: "))
        for i in self.permitidas:
            if b == i:
                if b in self.deno:
                    if self.deno[b] == 0:
                        print("no hay billetes de ese tipo dentro")
                    else:    
                        self.deno[b] = self.deno[b] - 1
                        print(f"Billete retirado {self.deno}")
                
    def anadir_pago(self):
        m = int(input("ingrese monto a pagar: "))
        self.cola_de_pagos.encolar(m)
   

    def realizar_pago(self):
        monto = self.cola_de_pagos.desencolar()
        self.permitidas.reverse()
        for den in self.permitidas:
            if den in self.deno:
                while self.deno[den] != 0 or monto != 0:
                    if den > monto or self.deno[den] == 0:
                        break
                    monto -= den
                    self.deno[den] = self.deno[den] - 1
    
def menu():
    caja = Caja({1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0, 500:0, 1000:0})  
    while True:
        print("1)agregar billete\n2)quitar billete\n3)añadir pago\n4)realizar pago\n5)Mostrar Caja\n6)salir")
        opcion = input("que quiere?: ")
        match opcion:
            case "1":
                caja.agregar()
                pass
            case "2":
                caja.quitar()
                pass
            case "3":
                caja.anadir_pago()
                pass
            case "4":
                caja.realizar_pago()
                pass
            case "5":
                print(caja.deno)
            case "6":
                break
            case _:
                print("Opción inválida")
                continue
            
menu()       
"""

class Caja:
    def __init__(self, denominacion):
        self.deno = denominacion
        self.permitidas = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        self.cola_de_pagos = Cola()

    def agregar(self):
        b = int(input("Ingrese el valor del billete: "))
        if b in self.permitidas:
            self.deno[b] += 1
            print(f"Billete de {b} agregado. Estado actual: {self.deno}")
        else:
            print("Billete no válido.")

    def quitar(self):
        b = int(input("Ingrese el valor del billete a retirar: "))
        if b in self.permitidas and self.deno[b] > 0:
            self.deno[b] -= 1
            print(f"Billete de {b} retirado. Estado actual: {self.deno}")
        elif b not in self.permitidas:
            print("Billete no válido.")
        else:
            print("No hay billetes de ese tipo.")

    def anadir_pago(self):
        m = int(input("Ingrese el monto del pago: "))
        self.cola_de_pagos.encolar(m)
        print(f"Pago de {m} añadido a la cola.")

    def realizar_pago(self):
        if self.cola_de_pagos.esta_vacio():
            print("No hay pagos pendientes.")
            return

        monto = self.cola_de_pagos.desencolar()
        print(f"Procesando pago de {monto}...")
        cambio = monto
        for den in sorted(self.permitidas, reverse=True):
            while cambio >= den and self.deno[den] > 0:
                cambio -= den
                self.deno[den] -= 1
                print(f"Entregado billete de {den}. Cambio restante: {cambio}")

        if cambio > 0:
            print(f"No se pudo completar el cambio. Faltan {cambio}.")
            self.cola_de_pagos.encolar(cambio)
        else:
            print("Pago realizado con éxito.")
        print(f"Estado actual de la caja: {self.deno}")

def menu():
    caja = Caja({1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0})
    while True:
        print("\n--- Menú ---")
        print("1) Agregar billete")
        print("2) Quitar billete")
        print("3) Añadir pago")
        print("4) Realizar pago")
        print("5) Mostrar caja")
        print("6) Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                caja.agregar()
            case "2":
                caja.quitar()
            case "3":
                caja.anadir_pago()
            case "4":
                caja.realizar_pago()
            case "5":
                print(f"Estado actual de la caja: {caja.deno}")
            case "6":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

menu()


