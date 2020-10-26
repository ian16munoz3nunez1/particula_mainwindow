from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Particula.mainclass import MainClass
from Particula.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.mainclass = MainClass()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)

    @Slot()
    def agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.mainclass.agregar_inicio(particula)
    
    @Slot()
    def agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.mainclass.agregar_final(particula)
    
    @Slot()
    def mostrar(self):
        self.ui.print.clear()
        self.ui.print.insertPlainText(str(self.mainclass))
        