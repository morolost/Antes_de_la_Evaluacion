from cola import Cola

# Importar la implementación de cola

cola = Cola()

class Impresora:
    def __init__(self, nombre, cap_tinta, tinta_res):
        self.nombres = nombre
        self.cap_tinta = cap_tinta
        self.tinta_res = tinta_res
        self.tareas = cola
        
    def encolar_documento(self, nombre_doc):
        self.tareas.encolar(nombre_doc)
        print(f"Documento '{nombre_doc}' encolado en la impresora {self.nombres}.")
    
    def imprimir_primero(self):
        if self.tareas.esta_vacio():
            print('no hay documentos encolados')
        elif self.tinta_res == 0:
            print('no tiene mas tinta')
        else:
            print("se imprimio un documento...")
            self.tinta_res - 1
            self.tareas.desencolar()
            
    def cargar_tinta(self):
        if self.tinta_res >= 0 and self.tinta_res < self.cap_tinta:
            print("El tanque se lleno")
            self.tinta_res =+ self.cap_tinta - self.tinta_res
        else:
            print("el tanque de tinta esta lleno")

class Oficina:
    def __init__(self):
        self.oficina = []
        
    def agregar_impresora(self):
        x = input('nombre de la impresora: ')
        e = int(input('ingrese capacidad maxima de tinta: '))
        impresora = Impresora(x, e, e)
        self.oficina.append(impresora)
        print(f"se creo la impresora {x} con capacidad de {e}")
        
    
    def quitar_impresora(self):
        x = 0
        print(f"Estas son las impresoras:")
        for i in (self.oficina):
            print(f"{x}- {i.nombres}")
            x =+ 1
        e = int(input("Que impresora quiere quitar?"))
        self.oficina.pop(e)
        
    def obtener_impresora_menos_documentos(self):
        b = 0
        for i in (self.oficina):
            if b >= len(i.tareas.cola):
                a = i.nombres 
            b = len(i.tareas.cola)
        print(f"la impresora con menor cantidad de documentos es {a}")
            
    def obtener_impresora_nombre(self):
        n = input("Ingrese el nombre de la impresora que desea: ")
        a = 0
        for i in self.oficina:
            if n == i.nombres:
                return a
            a =+ 1 
        print("no se encontro la impresora...")


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
                try:
                    oficina.agregar_impresora()
                except TypeError or ValueError:
                    print("error al dar datos")
                pass
            case "2":
                try:
                    n = oficina.obtener_impresora_nombre()
                    impresora = oficina.oficina[n]
                    n = input("Nombre del documento: ")
                    impresora.encolar_documento(n)
                except TypeError:
                    print("error con el nombre")
                pass
            case "3":
                try:
                    n = oficina.obtener_impresora_nombre()
                    impresora = oficina.oficina[n]
                    impresora.imprimir_primero()
                except TypeError:
                    print("error al dar nombre ")
                pass
            case "4":
                try:
                    n = oficina.obtener_impresora_nombre()
                    impresora = oficina.oficina[n]
                    impresora.cargar_tinta()
                except TypeError:
                    print("error con dar el nombre")
                pass
            case "5":
                oficina.obtener_impresora_menos_documentos()
                pass
            case "6":
                try:
                    oficina.quitar_impresora()
                except TypeError:
                    print("error con el nombre de la impresora")
                pass
            case "7":
                break
            case _:
                print("Opción inválida")
                continue
            
menu()    
            
