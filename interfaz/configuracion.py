from PyQt5.QtWidgets import *

class VentanaConfiguracion(QWidget):

    def __init__(self, problema, algoritmo, objetivo):
        super().__init__()

        self.setWindowTitle("Configuración")

        self.setGeometry(300, 300, 500, 400)

        layout = QVBoxLayout()

        titulo = QLabel("Configuración del Problema")
        titulo.setStyleSheet("font-size: 18px;")

        layout.addWidget(titulo)

        # Mostrar selección
        layout.addWidget(QLabel(f"Problema: {problema}"))
        layout.addWidget(QLabel(f"Algoritmo: {algoritmo}"))
        layout.addWidget(QLabel(f"Objetivo: {objetivo}"))

        # -------- PSO --------
        if "PSO" in algoritmo:

            self.particulas = QSpinBox()
            self.iteraciones = QSpinBox()

            self.particulas.setValue(30)
            self.iteraciones.setValue(100)

            layout.addWidget(QLabel("Número de partículas"))
            layout.addWidget(self.particulas)

            layout.addWidget(QLabel("Número de iteraciones"))
            layout.addWidget(self.iteraciones)

        # -------- GA --------
        elif "GA" in algoritmo:

            self.poblacion = QSpinBox()
            self.generaciones = QSpinBox()

            self.poblacion.setValue(50)
            self.generaciones.setValue(100)

            layout.addWidget(QLabel("Tamaño de población"))
            layout.addWidget(self.poblacion)

            layout.addWidget(QLabel("Número de generaciones"))
            layout.addWidget(self.generaciones)

        # Botones
        botonEjecutar = QPushButton("Ejecutar")

        botonVolver = QPushButton("Volver")

        layout.addWidget(botonEjecutar)
        layout.addWidget(botonVolver)

        self.setLayout(layout)