from PyQt5.QtWidgets import *
from interfaz.configuracion import VentanaConfiguracion

class MenuPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        # ==========================================
        # CONFIGURACIÓN VENTANA
        # ==========================================

        self.setWindowTitle("Metaheurísticas")
        self.setGeometry(200, 200, 500, 450)

        # ==========================================
        # LAYOUT PRINCIPAL
        # ==========================================

        layout = QVBoxLayout()

        # ==========================================
        # TÍTULO
        # ==========================================

        titulo = QLabel("Sistema de Metaheurísticas")
        titulo.setStyleSheet("font-size: 20px;")

        layout.addWidget(titulo)

        # ==========================================
        # TIPO DE PROBLEMA
        # ==========================================

        self.comboProblema = QComboBox()

        self.comboProblema.addItems([
            "Función continua",
            "Función binaria",
            "Función categórica",
            "Problema del Viajero (TSP)"
        ])

        self.comboProblema.currentTextChanged.connect(
            self.actualizarFunciones
        )

        layout.addWidget(QLabel("Tipo de problema"))
        layout.addWidget(self.comboProblema)

        # ==========================================
        # PROBLEMA ESPECÍFICO
        # ==========================================

        self.comboFuncion = QComboBox()

        layout.addWidget(QLabel("Problema específico"))
        layout.addWidget(self.comboFuncion)

        # ==========================================
        # ALGORITMOS
        # ==========================================

        self.comboAlgoritmo = QComboBox()

        self.comboAlgoritmo.addItems([
            "Algoritmo Genético (GA)",
            "Colonia de Hormigas (ACO)",
            "Enjambre de Partículas (PSO)",
            "Sistema Inmune Artificial (AIS)",
            "Evolución Diferencial (DE)"
        ])

        layout.addWidget(QLabel("Algoritmo"))
        layout.addWidget(self.comboAlgoritmo)

        # ==========================================
        # OBJETIVO
        # ==========================================

        self.maxRadio = QRadioButton("Maximizar")
        self.minRadio = QRadioButton("Minimizar")

        layout.addWidget(QLabel("Objetivo"))
        layout.addWidget(self.maxRadio)
        layout.addWidget(self.minRadio)

        # ==========================================
        # BOTÓN CONTINUAR
        # ==========================================

        boton = QPushButton("Continuar")

        boton.clicked.connect(self.abrirConfiguracion)

        layout.addWidget(boton)

        # ==========================================
        # CARGAR FUNCIONES INICIALES
        # ==========================================

        self.actualizarFunciones()

        # ==========================================
        # APLICAR LAYOUT
        # ==========================================

        self.setLayout(layout)

    # ==========================================
    # ACTUALIZAR FUNCIONES
    # ==========================================

    def actualizarFunciones(self):

        self.comboFuncion.clear()

        problema = self.comboProblema.currentText()

        # ==========================================
        # CONTINUAS
        # ==========================================

        if problema == "Función continua":

            self.comboFuncion.addItems([
                "Sphere",
                "Rastrigin",
                "Rosenbrock"
            ])

        # ==========================================
        # BINARIAS
        # ==========================================

        elif problema == "Función binaria":

            self.comboFuncion.addItems([
                "OneMax",
                "Binario Inverso"
            ])

        # ==========================================
        # CATEGÓRICAS
        # ==========================================

        elif problema == "Función categórica":

            self.comboFuncion.addItems([
                "Color Matching"
            ])

        # ==========================================
        # TSP
        # ==========================================

        elif problema == "Problema del Viajero (TSP)":

            self.comboFuncion.addItems([
                "Traveling Salesman Problem"
            ])

    # ==========================================
    # ABRIR CONFIGURACIÓN
    # ==========================================

    def abrirConfiguracion(self):

        problema = self.comboProblema.currentText()

        funcion = self.comboFuncion.currentText()

        algoritmo = self.comboAlgoritmo.currentText()

        if self.maxRadio.isChecked():
            objetivo = "Maximización"
        else:
            objetivo = "Minimización"

        self.ventana = VentanaConfiguracion(
            problema,
            funcion,
            algoritmo,
            objetivo
        )

        self.ventana.show()