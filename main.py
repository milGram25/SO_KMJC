
from PyQt5 import QtWidgets
from interfaz import Ui_Dialog
from enfermos import Proceso, quicksort
import sys
from PyQt5.QtCore import QThread, pyqtSignal

class ProcesoThread(QThread):
    actualizar=pyqtSignal(str)

    def __init__(self, proceso):
        super().__init__()
        self.proceso = proceso
    
    def run(self):
        restante = self.proceso.tiempo    
        while restante > 0:
            self.actualizar.emit(f'Ejecutando {self.proceso.nombre}, tiempo restante: {restante} segundos\n')
            self.sleep(1)  # Simula el tiempo de ejecución
            restante -= 1
        self.actualizar.emit(f'Proceso {self.proceso.nombre} finalizado.\n')


# Crear la clase principal que se extiende de QDialog
class VentanaPrincipal(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.fila = []  # Lista para almacenar los procesos
        self.ui.ButtonProces.clicked.connect(self.agregar_proceso)
        self.ui.ButtonEjecutar.clicked.connect(self.ejecutar_proceso)
        self.ui.ButtonCancelar.clicked.connect(self.cancelar_proceso)


    def agregar_proceso(self):
        nombre=self.ui.lineNameProceso.text()
        tiempo_texto= self.ui.lineProceso.text()

        if not nombre or not tiempo_texto.isdigit():
            return  # Validar entrada

        tiempo = int(tiempo_texto)
        nuevo_proceso = Proceso(nombre, tiempo)
        self.fila.append(nuevo_proceso)
        self.fila = quicksort(self.fila)  # Ordenar la lista de procesos
        self.actualizar_scroll()
        self.ui.lineNameProceso.clear()
        self.ui.lineProceso.clear()
    
    def actualizar_scroll(self):
        layout = QtWidgets.QVBoxLayout()
        for proceso in self.fila:
            etiqueta = QtWidgets.QLabel(f'{proceso.nombre} - {proceso.tiempo} segundos')
            layout.addWidget(etiqueta)
        # Limpia y actualiza el contenido anterior del scroll area
        old_layout = self.ui.scrollAreaWidgetContents.layout()
        if old_layout is not None:
            QtWidgets.QWidget().setLayout(old_layout)
        self.ui.scrollAreaWidgetContents.setLayout(layout)
        #Muestra en tiempo total de espera
        total=sum(p.tiempo for p in self.fila)
        self.ui.textBrowserInProcess.setText(f'Tiempo total de espera: {total} segundo(s)')
    
    def ejecutar_proceso(self):
        if not self.fila:
            self.ui.textBrowserInProcess.setText("No hay procesos en la fila")
            return

        proceso=self.fila.pop(0)
        self.actualizar_scroll()

        self.thread=ProcesoThread(proceso)
        self.thread.actualizar.connect(self.ui.textBrowserInProcess.setText)
        self.thread.start()
    
    def cancelar_proceso(self):
        if isinstance(getattr(self, 'thread', None), QThread) and self.thread.isRunning():
            self.thread.terminate()
            #terminate() detiene el hilo abruptamente. 
            # No es lo más elegante, pero para esto es funcional 
            self.ui.textBrowserInProcess.setText("Proceso Cancelado")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())