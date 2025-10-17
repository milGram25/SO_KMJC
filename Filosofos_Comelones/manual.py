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

    def comer(self):
        # Aumenta el tiempo de comer del filósofo
        self.tiempo_comer += 3
        self.label.setStyleSheet("background-color: green; color: white;")
        self.label.setToolTip(f"{self.tiempo_comer} segundos comiendo")
        print(f'Filosofo {self.id}: {self.tiempo_comer} segundos comiendo')

    def no_comer(self):
        self.label.setStyleSheet("background-color: red; color: white;")
        self.label.setToolTip("")

# Clase prinicipal para controlar la interfaz y la lógica
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
        turno = random.randint(0, 4)
        self.comiendo1 = self.filosofos[turno]
        self.comiendo2 = self.filosofos[turno - 3] if turno >= 3 else self.filosofos[turno + 2]

        #Temporizador para el ciclo de comer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_turno)

        # Conectar botones a funciones
        self.ui.pushButtonComer.clicked.connect(self.comer)
        self.ui.pushButtonNoComer.clicked.connect(self.no_comer)

    def comer(self):
        self.timer.start(3000)  # Actualiza cada 5 segundos

    def no_comer(self):
        self.timer.stop()
        for f in self.filosofos:
            f.tiempo_comer = 0
            f.no_comer()
    
    def actualizar_turno(self):
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
            self.contador = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mesa = Mesa()
    mesa.show()
    sys.exit(app.exec_())