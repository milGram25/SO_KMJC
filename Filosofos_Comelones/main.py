import random
import time

# Clase que representa a un filósofo
class Filosofo:
    def __init__(self, id):
        self.id = id
        self.tiempo_comer = 0

    def __str__(self):
        return f'Filosofo {self.id}: {self.tiempo_comer} segundos comiendo'
    
# Crear filosofos
for i in range(5):
    Filosofo(i)

#Elegir los filosofos que comen primero
turno = random.randint(0,4)
comiendo1 = Filosofo(turno)
#Si el indice se desborda, se va a los primeros, para hacer una lsita circular
comiendo2 = Filosofo(turno-3 if turno>=3 else turno+2)

#Funcion para que los filosofos coman
def comer(filosofo):
    #Aumenta el tiempo de comer de los filósofos que están comiendo
    filosofo.tiempo_comer += 5
    print(filosofo)
    print('Ya comio 1')

    #Avanza el turno a los siguientes filósofos
    return Filosofo(avanzar(comiendo1))
    
def avanzar(filosofo):
    if filosofo.id == 4:
        return filosofo.id - 4
    else:
        return filosofo.id + 1

while True:
    comiendo1=comer(comiendo1)
    comiendo2=comer(comiendo2)
    time_sleep = random.randint(1,3)
    time.sleep(time_sleep)