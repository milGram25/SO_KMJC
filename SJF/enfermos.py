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
    pivot=arr[0]
    less=[x for x in arr[1:] if x.tiempo < pivot.tiempo]
    greater = [x for x in arr[1:] if x.tiempo >= pivot.tiempo]
    return quicksort(less) + [pivot] + quicksort(greater)
    '''else:
        #Elige el primer proceso como pivote
        pivot = arr[0]
        #Procesos con tiempo menor al pivote
        less_than_pivot = [x for x in arr[1:] if x.tiempo < pivot.tiempo]
        #Procesos con tiempo mayor o igual al pivote
        greater_than_pivot = [x for x in arr[1:] if x.tiempo >= pivot.tiempo]
        #Ordena recursivamente y combina las listas con el pivote en el medio
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)'''

#Crea una lista con tres procesos, cada uno con nombre y tiempo de ejecución
fila = []
