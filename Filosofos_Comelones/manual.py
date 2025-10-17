from PyQt5 import QtCore, QtGui, QtWidgets
from mesita import Ui_Dialog
import sys
import random
import time

# Clase que representa a un filósofo
class Filosofo:
    def __init__(self, id, label):
        self.id = id
        self.label = label
        self.tiempo_comer = 0
        self.comiendo = False

    def comer(self, tiempo):
        # Aumenta el tiempo de comer del filósofo
        ##### Cambiar tiempo de comer de los filósofos
        self.tiempo_comer += tiempo/1000  # Convertir milisegundos a segundos
        self.label.setStyleSheet("background-color: green; color: white;")
        self.label.setToolTip(f"{self.tiempo_comer} segundos comiendo")
        print(f'Filosofo {self.id}: {self.tiempo_comer} segundos comiendo')

    def no_comer(self):
        self.label.setStyleSheet("background-color: red; color: white;")
        self.label.setToolTip("")

# Clase prinicipal para controlar la interfaz y la lógica
# Soy un papu pro
class Mesa(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.contador = 0
        self.estado = "comiendo"

        # Crear filósofos y asociar etiquetas
        self.filosofos = [
            Filosofo(0, self.ui.labelFilo0),
            Filosofo(1, self.ui.labelFilo1),
            Filosofo(2, self.ui.labelFilo2),
            Filosofo(3, self.ui.labelFilo3),
            Filosofo(4, self.ui.labelFilo4)
        ]

        # Elegir los filósofos que comen primero
        while True:
            time.sleep(random.randint(3, 5))
            turno = random.randint(0, 4)
            quererComer(self.filosofos, turno)
            if (random.randint(0,1) == 0):
                break
        

        #Temporizador para el ciclo de comer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_turno)

        # Conectar botones a funciones
        self.ui.pushButtonComer.clicked.connect(self.comer)
        self.ui.pushButtonNoComer.clicked.connect(self.no_comer)

##### Cambiar tiempo de comer de los filósofos
def comer(filosofo):
    tiempo_comer = random.randint(1000, 10000)  # Tiempo aleatorio entre 1 y 3 segundos
    filosofo.timer.start(tiempo_comer)  # Actualiza cada 5 segundos
    filosofo.comer(tiempo_comer)

def no_comer(self):
    self.timer.stop()
    for f in self.filosofos:
        f.tiempo_comer = 0
        f.no_comer()
    
    """def actualizar_turno(self):
        if self.estado == "comiendo":
            for f in self.filosofos:
                f.no_comer()
            self.comiendo1.comer()
            self.comiendo2.comer()
            self.contador += 1
        
            if self.contador >= 5:
                self.estado = "pensando"
                self.contador = 0
        elif self.estado == "pensando":
            for f in self.filosofos:
                f.no_comer()
            self.contador += 1

        if self.contador >= 1:
            # Cambio de turno
            self.comiendo1 = self.filosofos[(self.comiendo1.id + 1) % 5]
            self.comiendo2 = self.filosofos[(self.comiendo2.id + 1) % 5]
            self.estado= "comiendo"
            self.contador = 0"""
    
# Elegir el segundo filósofo que come
def quererComer(filosofos, turno):
    # Si el índice se desborda, se va a los primeros, para hacer una lista circular
    if (filosofos[turno+1].comiendo == True or filosofos[turno-1].comiendo == True):
        return
    else:
        filosofos[turno].estado = "comiendo"
        empezarComer(filosofos[turno])
        return
        
def empezarComer(filosofo):
        tiempo_comer = random.randint(1000, 10000)  # Tiempo aleatorio entre 1 y 3 segundos
        filosofo.timer.start(tiempo_comer)  # Actualiza cada 5 segundos
        filosofo.comer(tiempo_comer)
        filosofo.timer = QtCore.QTimer()
        filosofo.timer.timeout.connect(filosofo.no_comer)
        
#Funcion para avanzar

#Funcion para retroceder


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mesa = Mesa()
    mesa.show()
    sys.exit(app.exec_())