from cola import Cola

cola = Cola()

class Impresora:
    def __init__(self, cap_max, nombre):
        self.nombre = nombre
        self.cap_max = cap_max
        self.documento = cola
        self.tinta = self.cap_max
    
    def encolar_documento(self):
        e = input("nombre del documento: ")
        self.documento.encolar(e)
        
    def imprimir_documento(self):
        if self.cap_max <= 0:
            print("no se puede imprimir el documento, cambie el cartucho de tinta...")
        else:
            print(f"se imprimio: {self.documento.cola[0]}")
            self.documento.desencolar(0)
            self.tinta - 1
    def cargar_tinta(self):
        if self.tinta < self.cap_max and self.tinta >= 0:
            self.tinta += self.cap_max - self.tinta
            
        

class Oficina:
    def __init__(self):
        self.oficina = cola
    
    def agregar_impresora(self):
        n = input("ingrese nombre de la impresora: ")
        c = int(input("ingrese capacidad maxima de la tinta: "))
        impresora = Impresora(c, n)
        self.oficina.encolar(impresora)
        
    def obtener_impresora_nombre(self):
        n = input("ingrese nombre de la impresora: ")
        for i in self.oficina.cola:
            if i.nombre == n:
                impresora = i
                return impresora
            else:
                print("no existe ese nombre")
    
    def quitar_impresora_nombre(self):
        n = input("ingresar nombre de la impresora: ")
        for i in self.oficina.cola:
            if i.nombre == n:
                self.oficina.desencolar(i)
                return
            else:
                print("no existe ese nombre")
    
    def impresora_menos_documentos(self):
        l = 0
        for i in self.oficina.cola:
            if len(i.documento.cola) <= l:
                nombre = i.nombre
            l = len(i.documento.cola)
        return nombre    
                

                
                
            


# Menú para interactuar con las impresoras y la oficina
def menu():
    oficina = Oficina()
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar impresora")
        print("2. Encolar documento")
        print("3. Imprimir documento")
        print("4. Cargar tinta")
        print("5. Obtener impresora libre")
        print("6. Quitar impresora")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                oficina.agregar_impresora()
                pass
            case "2":
                impresora = oficina.obtener_impresora_nombre()
                impresora.encolar_documento()
                pass
            case "3":
                impresora = oficina.obtener_impresora_nombre()
                impresora.imprimir_documento()
                pass
            case "4":
                impresora = oficina.obtener_impresora_nombre()
                impresora.cargar_tinta()
                pass
            case "5":
                oficina.impresora_menos_documentos()
                pass
            case "6":
                oficina.obtener_impresora_nombre()
                pass
            case "7":
                break
            case _:
                print("Opción inválida")
                continue
            
menu()    
            
