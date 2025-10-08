#Algoritmo de Planificación - Shortest Job First
import time
#Define la clase

class Proceso:
    #Creaci[on del contructor de la clase]
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo

def quicksort(arr):
    #Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        #Elige el primer proceso como pivote
        pivot = arr[0]
        #Procesos con tiempo menor al pivote
        less_than_pivot = [x for x in arr[1:] if x.tiempo < pivot.tiempo]
        #Procesos con tiempo mayor o igual al pivote
        greater_than_pivot = [x for x in arr[1:] if x.tiempo >= pivot.tiempo]
        #Ordena recursivamente y combina las listas con el pivote en el medio
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

#Crea una lista con tres procesos, cada uno con nombre y tiempo de ejecución
fila = [Proceso('Opera', 10), Proceso('Calculadora', 8), Proceso('Word', 9)]
fila = quicksort(fila)
#Ordenar la lista de procesos por tiempo de ejecución restante

def agregar_proceso(nombre, tiempo, fila):
    fila.append(Proceso(nombre, tiempo))
    #Ordena la lista usando la función quicksort
    return quicksort(fila)

def mostrar_fila(fila):
    print("Fila de procesos ordenada por tiempo de ejecución:")
    for proceso in fila:
        print(proceso.nombre, '-', proceso.tiempo,' segundos\n')

mostrar_fila(fila)

#Ejecutar proceso
def ejecutar_proceso(proceso):
    restante = proceso.tiempo    
    while restante > 0:
        print(f'Ejecutando {proceso.nombre}, tiempo restante: {restante} segundos')
        restante -= 1
        time.sleep(1)  # Simula el tiempo de ejecución
    print(f'Proceso {proceso.nombre} finalizado.\n')

def menu(fila):
    opcion = 0
    while opcion != 3:
        print("Menú de opciones:")
        print("1. Agregar proceso")
        print("2. Ejecutar siguiente proceso")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                nombre = input("Ingrese el nombre del proceso: ")
                tiempo = int(input("Ingrese el tiempo de ejecución (en segundos): "))
                fila = agregar_proceso(nombre, tiempo, fila)                
            case '2':
                if len(fila) > 0:
                    proceso = fila[0]
                    ejecutar_proceso(proceso)
                    time.sleep(2)  # Simula espera entre procesos
                    fila.pop(0)  # Elimina el proceso que acaba de finalizar
                else:
                    print("No hay procesos en la fila.")
            case '3':
                print("Saliendo del programa.")
                return
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_fila(fila)
    menu(fila)