#Algoritmo de Planificación - Shortest Job First

#Define la clase
class Proceso:
    #Creaci[on del contructor de la clase]
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo

#Crea una lista con tres procesos, cada uno con nombre y tiempo de ejecución
fila = [Proceso('Opera', 10), Proceso('Calculadora', 8), Proceso('Word', 9)]
arr = [proceso.tiempo for proceso in fila]

#Ordenar la lista de procesos por tiempo de ejecución restante
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

def agregar_proceso(nombre, tiempo, fila):
    fila.append(Proceso(nombre, tiempo))
    #Ordena la lista usando la función quicksort
    fila = quicksort(fila)
    return fila

def mostrar_fila(fila):
    print("Fila de procesos ordenada por tiempo de ejecución:")
    for proceso in fila:
        print(proceso.nombre, '-', proceso.tiempo,' segundos\n')

#Ejemplo de uso
agregar_proceso('Excel', 3, fila)
agregar_proceso('PowerPoint', 14, fila)
agregar_proceso('Visual Studio Code', 18, fila)
agregar_proceso('Spotify', 20, fila)

mostrar_fila(fila)
        
#Ejecutar proceso
def ejecutar_proceso(fila):
    for Proceso.tiempo in fila:
        restante = Proceso.tiempo-1
        while restante > 0:
            print(f'Ejecutando {Proceso.nombre}, tiempo restante: {restante} segundos')
            restante -= 1
        print(f'Proceso {Proceso.nombre} finalizado.\n')    
    fila.remove(Proceso)
    return fila

ejecutar_proceso(fila)