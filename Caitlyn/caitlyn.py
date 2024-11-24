from pila import Pila

pila = Pila()

"""
class Arma:
    def __init__(self, nombre, daño):
        self.balas = Pila()
        self.nombre = nombre
        self.daño = daño

    def stackeo(self):
        if len(self.balas.pila) >= 5:
            print("¡Golpe crítico!")
            while not self.balas.esta_vacia():
                self.balas.desapilar()
            return self.daño * 2
        else:
            return self.daño

    def agregar_balas(self):
        self.balas.apilar("bala")
        print(f"Conteo de disparos: {len(self.balas.pila)}")


class Enemigo:
    def __init__(self, vida):
        self.vida = vida

    def recibir_daño(self, daño):
        self.vida -= daño
        print(f"VIDA RESTANTE DEL ENEMIGO: {self.vida}")

    def esta_muerto(self):
        if self.vida <= 0:
            print("El enemigo ha muerto.")
            return True
        return False


class Caitlyn:
    def __init__(self):
        self.armas = []
        self.enemigos = []

    def crear_arma(self):
        try:
            nombre = input("Ingrese el nombre del arma: ")
            daño = int(input("Ingrese el daño del arma: "))
            arma = Arma(nombre, daño)
            self.armas.append(arma)
            print(f"Se creó el arma {nombre} con daño {daño}.")
        except ValueError:
            print("Error: Ingrese un número válido para el daño.")

    def crear_enemigo(self):
        try:
            vida = int(input("Ingrese la vida del enemigo: "))
            enemigo = Enemigo(vida)
            self.enemigos.append(enemigo)
            print(f"Se creó un enemigo con vida {vida}.")
        except ValueError:
            print("Error: Ingrese un número válido para la vida.")

    def disparar(self):
        if not self.armas:
            print("No tienes armas creadas.")
            return

        if not self.enemigos:
            print("No hay enemigos para disparar.")
            return

        print("Caitlyn dispara...")
        arma = self.armas[0]
        enemigo = self.enemigos[0]

        arma.agregar_balas()
        daño = arma.stackeo()
        enemigo.recibir_daño(daño)

        if enemigo.esta_muerto():
            print("Enemigo eliminado de la lista.")
            self.enemigos.pop(0)


def menu():
    caitlyn = Caitlyn()

    while True:
        print("\n--- Menú ---")
        print("1. Disparar")
        print("2. Crear Arma")
        print("3. Crear Enemigo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            match opcion:
                case "1":
                    caitlyn.disparar()
                case "2":
                    caitlyn.crear_arma()
                case "3":
                    caitlyn.crear_enemigo()
                case "4":
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f"Error inesperado: {e}")


menu()    
"""
#y dar un ejemplo parecido con 2 classes

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} | Prioridad: {self.prioridad} | Estado: {estado}"


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        nueva_tarea = Tarea(descripcion, prioridad)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada con prioridad {prioridad}.")

    def listar_tareas(self):
        if not self.tareas:
            print("No tienes tareas en tu lista.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    def completar_tarea(self, numero):
        if 0 < numero <= len(self.tareas):
            self.tareas[numero - 1].completar()
            print(f"Tarea '{self.tareas[numero - 1].descripcion}' marcada como completada.")
        else:
            print("Número de tarea inválido.")

    def eliminar_tarea(self, numero):
        if 0 < numero <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(numero - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        else:
            print("Número de tarea inválido.")


def menu():
    nombre = input("Ingrese su nombre: ")
    persona = Persona(nombre)
    print(f"\n¡Hola, {persona.nombre}! Bienvenido a tu gestor de tareas.\n")

    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                descripcion = input("Descripción de la tarea: ")
                try:
                    prioridad = int(input("Prioridad de la tarea (1-5): "))
                    if 1 <= prioridad <= 5:
                        persona.agregar_tarea(descripcion, prioridad)
                    else:
                        print("La prioridad debe estar entre 1 y 5.")
                except ValueError:
                    print("Por favor, ingresa un número válido para la prioridad.")
            case "2":
                persona.listar_tareas()
            case "3":
                try:
                    numero = int(input("Número de la tarea a completar: "))
                    persona.completar_tarea(numero)
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            case "4":
                try:
                    numero = int(input("Número de la tarea a eliminar: "))
                    persona.eliminar_tarea(numero)
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            case "5":
                print("Saliendo del gestor de tareas. ¡Hasta pronto!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


menu()