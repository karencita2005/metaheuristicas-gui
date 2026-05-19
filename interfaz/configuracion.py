from PyQt5.QtWidgets import *

from algoritmos.pso import ejecutar_pso
from algoritmos.ga import ejecutar_ga

from problemas.continuas import *
from problemas.binarias import *
from problemas.categoricas import *

class VentanaConfiguracion(QWidget):

    def __init__(self, problema, funcion, algoritmo, objetivo):
        super().__init__()

        self.algoritmo = algoritmo
        self.funcion = funcion

        self.setWindowTitle("Configuración")

        self.setGeometry(300, 300, 500, 450)

        layout = QVBoxLayout()

        titulo = QLabel("Configuración")
        titulo.setStyleSheet("font-size: 18px;")

        layout.addWidget(titulo)

        layout.addWidget(QLabel(f"Problema: {problema}"))
        layout.addWidget(QLabel(f"Función: {funcion}"))
        layout.addWidget(QLabel(f"Algoritmo: {algoritmo}"))
        layout.addWidget(QLabel(f"Objetivo: {objetivo}"))

        # ==========================================
        # PSO
        # ==========================================

        if "PSO" in algoritmo:

            self.particulas = QSpinBox()
            self.particulas.setValue(30)

            layout.addWidget(QLabel("Número de partículas"))
            layout.addWidget(self.particulas)

            self.iteraciones = QSpinBox()
            self.iteraciones.setValue(100)

            layout.addWidget(QLabel("Número de iteraciones"))
            layout.addWidget(self.iteraciones)

        # ==========================================
        # GA
        # ==========================================

        elif "GA" in algoritmo:

            self.poblacion = QSpinBox()
            self.poblacion.setValue(50)

            layout.addWidget(QLabel("Tamaño población"))
            layout.addWidget(self.poblacion)

            self.generaciones = QSpinBox()
            self.generaciones.setValue(100)

            layout.addWidget(QLabel("Generaciones"))
            layout.addWidget(self.generaciones)

        # ==========================================
        # BOTONES
        # ==========================================

        botonEjecutar = QPushButton("Ejecutar")

        botonEjecutar.clicked.connect(
            self.ejecutarAlgoritmo
        )

        layout.addWidget(botonEjecutar)

        self.setLayout(layout)

    # ==========================================
    # OBTENER FUNCIÓN
    # ==========================================

    def obtenerFuncion(self):

        funciones = {

            # Continuas
            "Sphere": sphere,
            "Rastrigin": rastrigin,
            "Rosenbrock": rosenbrock,

            # Binarias
            "OneMax": onemax,
            "Binario Inverso": binario_inverso,

            # Categórica
            "Color Matching": color_matching
        }

        return funciones[self.funcion]

    # ==========================================
    # EJECUTAR
    # ==========================================

    def ejecutarAlgoritmo(self):

        funcion = self.obtenerFuncion()

        # ==========================================
        # PSO
        # ==========================================

        if "PSO" in self.algoritmo:

            particulas = self.particulas.value()

            iteraciones = self.iteraciones.value()

            mejor_posicion, mejor_fitness, historial = ejecutar_pso(
                funcion,
                particulas,
                iteraciones
            )

            QMessageBox.information(
                self,
                "Resultado",

                f"Mejor posición:\n{mejor_posicion}\n\n"
                f"Fitness:\n{mejor_fitness}"
            )

        # ==========================================
        # GA
        # ==========================================

        elif "GA" in self.algoritmo:

            poblacion = self.poblacion.value()

            generaciones = self.generaciones.value()

            mejor, fitness, historial = ejecutar_ga(
                funcion,
                poblacion,
                generaciones
            )

            QMessageBox.information(
                self,
                "Resultado",

                f"Mejor individuo:\n{mejor}\n\n"
                f"Fitness:\n{fitness}"
            )