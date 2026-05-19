from PyQt5.QtWidgets import *
from interfaz.configuracion import VentanaConfiguracion

class MenuPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        # ==========================================
        # VENTANA
        # ==========================================

        self.setWindowTitle("Sistema de Metaheurísticas")
        self.setGeometry(200, 200, 600, 500)

        layout = QVBoxLayout()

        # ==========================================
        # TÍTULO
        # ==========================================

        titulo = QLabel("Sistema de Metaheurísticas")
        titulo.setStyleSheet("font-size: 22px;")

        layout.addWidget(titulo)

        # ==========================================
        # TIPO PROBLEMA
        # ==========================================

        self.comboProblema = QComboBox()

        self.comboProblema.addItems([
            "Función continua",
            "Función binaria",
            "Función categórica",
            "Problema del Viajero (TSP)"
        ])

        self.comboProblema.currentTextChanged.connect(
            self.actualizarProblemas
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

        layout.addWidget(QLabel("Algoritmo"))
        layout.addWidget(self.comboAlgoritmo)

        # ==========================================
        # OBJETIVO
        # ==========================================

        self.maxRadio = QRadioButton("Maximización")
        self.minRadio = QRadioButton("Minimización")

        self.minRadio.setChecked(True)

        layout.addWidget(QLabel("Objetivo"))
        layout.addWidget(self.maxRadio)
        layout.addWidget(self.minRadio)

        # ==========================================
        # BOTÓN
        # ==========================================

        boton = QPushButton("Continuar")

        boton.clicked.connect(self.abrirConfiguracion)

        layout.addWidget(boton)

        # ==========================================
        # INICIALIZAR
        # ==========================================

        self.actualizarProblemas()

        self.setLayout(layout)

    # ==========================================
    # ACTUALIZAR PROBLEMAS
    # ==========================================

    def actualizarProblemas(self):

        self.comboFuncion.clear()
        self.comboAlgoritmo.clear()

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

            self.comboAlgoritmo.addItems([
                "Algoritmo Genético (GA)",
                "Enjambre de Partículas (PSO)",
                "Sistema Inmune Artificial (AIS)",
                "Evolución Diferencial (DE)"
            ])

        # ==========================================
        # BINARIAS
        # ==========================================

        elif problema == "Función binaria":

            self.comboFuncion.addItems([
                "OneMax",
                "Binario Inverso"
            ])

            self.comboAlgoritmo.addItems([
                "Algoritmo Genético (GA)",
                "Sistema Inmune Artificial (AIS)"
            ])

        # ==========================================
        # CATEGÓRICAS
        # ==========================================

        elif problema == "Función categórica":

            self.comboFuncion.addItems([
                "Color Matching"
            ])

            self.comboAlgoritmo.addItems([
                "Algoritmo Genético (GA)"
            ])

        # ==========================================
        # TSP
        # ==========================================

        elif problema == "Problema del Viajero (TSP)":

            self.comboFuncion.addItems([
                "Traveling Salesman Problem"
            ])

            self.comboAlgoritmo.addItems([
                "Algoritmo Genético (GA)",
                "Colonia de Hormigas (ACO)"
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