from PyQt5.QtWidgets import *
from interfaz.configuracion import VentanaConfiguracion

class MenuPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Metaheurísticas")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        titulo = QLabel("Sistema de Metaheurísticas")
        titulo.setStyleSheet("font-size: 20px;")

        # Combo Problema
        self.comboProblema = QComboBox()

        self.comboProblema.addItems([
         "Función continua",
         "Función binaria",
         "Función categórica",
         "Problema del Viajero (TSP)"
        ])

        # Combo Algoritmo
        self.comboAlgoritmo = QComboBox()

        self.comboAlgoritmo.addItems([
         "Algoritmo Genético (GA)",
         "Colonia de Hormigas (ACO)",
         "Enjambre de Partículas (PSO)",
         "Sistema Inmune Artificial (AIS)",
         "Evolución Diferencial (DE)"
        ])

        # Objetivo
        self.maxRadio = QRadioButton("Maximizar")
        self.minRadio = QRadioButton("Minimizar")

        # Botón
        boton = QPushButton("Continuar")
        boton.clicked.connect(self.abrirConfiguracion)

        layout.addWidget(titulo)

        layout.addWidget(QLabel("Tipo de problema"))
        layout.addWidget(self.comboProblema)

        layout.addWidget(QLabel("Algoritmo"))
        layout.addWidget(self.comboAlgoritmo)

        layout.addWidget(QLabel("Objetivo"))
        layout.addWidget(self.maxRadio)
        layout.addWidget(self.minRadio)

        layout.addWidget(boton)

        self.setLayout(layout)

    def abrirConfiguracion(self):

        problema = self.comboProblema.currentText()

        algoritmo = self.comboAlgoritmo.currentText()

        if self.maxRadio.isChecked():
            objetivo = "Maximización"
        else:
            objetivo = "Minimización"

        self.ventana = VentanaConfiguracion(
            problema,
            algoritmo,
            objetivo
        )

        self.ventana.show()