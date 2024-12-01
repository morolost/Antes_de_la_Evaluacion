from cola import Cola
cola = Cola()
class Caja:
    def __init__(self,denominacion):
        self.deno = denominacion
        self.permitidas = [1,2,5,10,20,50,100,200,500,1000]
        self.cola_de_pagos = cola
        
    def agregar(self):
        x = int(input("billete a agregar: "))
        for i in self.permitidas:
            if i == x:
                self.deno[x] = self.deno[x] + 1
                print(f"Billete agregado. Estado actual: {self.deno}")
                return
      
    def quitar(self):
        x = int(input("billete a sacar: "))
        for i in self.permitidas:
            if i == x and self.deno[i] != 0:
                self.deno[x] = self.deno[x] - 1
                print(f"Billete extraido. Estado actual: {self.deno}")
                return
                
    def agregar_pago(self):
        x = int(input("ingrese monto a pagar: "))
        self.cola_de_pagos.encolar(x)
    """  
    def realizar_pago(self):
        m = self.cola_de_pagos.desencolar()
        self.permitidas.reverse()
        for i in self.permitidas:
            while self.deno[i] != 0 and m != 0:
                if i > m or self.deno[i] == 0:
                    break
                m -= i
                self.deno[i] -= 1
    """ 
    def realizar_pago(self):
        if self.cola_de_pagos.esta_vacio():
            print("no hay pagos pendientes")
        
        monto = self.cola_de_pagos.desencolar()
        self.permitidas.reverse()
        for i in self.permitidas:
            while monto >= i and self.deno[i] > 0:
                if i > monto or self.deno[i] == 0:
                        break
                monto -= i
                self.deno[i] -= 1
        
        if monto > 0:
            print("pago no realizado falta plata")
            self.cola_de_pagos.encolar(monto)
        else:
            print("pago realizado")
                
        
                    
                        
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
                caja.agregar_pago()
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
                        
                        
                    
                    