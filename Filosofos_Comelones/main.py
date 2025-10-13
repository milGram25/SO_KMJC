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
filosofos=[]
for i in range(5):
    filosofos.append(Filosofo(i))

#Elegir los filosofos que comen primero
turno = random.randint(0,4)
comiendo1 = filosofos[turno]
#Si el indice se desborda, se va a los primeros, para hacer una lsita circular
comiendo2 = filosofos[turno-3] if turno >= 3 else filosofos[turno+2]

#Funcion para que los filosofos coman
def comer(filosofo):
    #Aumenta el tiempo de comer de los filósofos que están comiendo
    filosofo.tiempo_comer += 1
    print(filosofo)
    return

while True:
    #Empiezan a comer los dos filosofos
    for i in range(5):
        comer(comiendo1)
        comer(comiendo2)
        time.sleep(1)
    
    #Cambian los filosofos que estan comiendo
    comiendo1 = filosofos[comiendo1.id-4] if comiendo1.id == 4 else filosofos[comiendo1.id+1]
    comiendo2 = filosofos[comiendo2.id-4] if comiendo2.id == 4 else filosofos[comiendo2.id+1]
    print('---')
    time_sleep = random.randint(1,3)
    time.sleep(time_sleep)