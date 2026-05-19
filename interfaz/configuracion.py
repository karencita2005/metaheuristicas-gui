from PyQt5.QtWidgets import *
from algoritmos.pso import ejecutar_pso

class VentanaConfiguracion(QWidget):

    def __init__(self, problema, funcion, algoritmo, objetivo):
        super().__init__()

        # ==========================================
        # GUARDAR DATOS
        # ==========================================

        self.algoritmo = algoritmo
        self.funcion = funcion

        # ==========================================
        # CONFIGURACIÓN VENTANA
        # ==========================================

        self.setWindowTitle("Configuración")
        self.setGeometry(300, 300, 500, 400)

        # ==========================================
        # LAYOUT PRINCIPAL
        # ==========================================

        layout = QVBoxLayout()

        # ==========================================
        # TÍTULO
        # ==========================================

        titulo = QLabel("Configuración del Problema")
        titulo.setStyleSheet("font-size: 18px;")

        layout.addWidget(titulo)

        # ==========================================
        # INFORMACIÓN
        # ==========================================

        layout.addWidget(QLabel(f"Problema: {problema}"))
        layout.addWidget(QLabel(f"Función: {funcion}"))
        layout.addWidget(QLabel(f"Algoritmo: {algoritmo}"))
        layout.addWidget(QLabel(f"Objetivo: {objetivo}"))

        # ==========================================
        # CONFIGURACIÓN PSO
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
        # CONFIGURACIÓN GA
        # ==========================================

        elif "GA" in algoritmo:

            self.poblacion = QSpinBox()
            self.poblacion.setValue(50)

            layout.addWidget(QLabel("Tamaño de población"))
            layout.addWidget(self.poblacion)

            self.generaciones = QSpinBox()
            self.generaciones.setValue(100)

            layout.addWidget(QLabel("Número de generaciones"))
            layout.addWidget(self.generaciones)

        # ==========================================
        # BOTONES
        # ==========================================

        botonEjecutar = QPushButton("Ejecutar")
        botonVolver = QPushButton("Volver")

        botonEjecutar.clicked.connect(self.ejecutarAlgoritmo)

        layout.addWidget(botonEjecutar)
        layout.addWidget(botonVolver)

        # ==========================================
        # APLICAR LAYOUT
        # ==========================================

        self.setLayout(layout)

    # ==========================================
    # EJECUTAR ALGORITMO
    # ==========================================

    def ejecutarAlgoritmo(self):

        # ==========================================
        # PSO
        # ==========================================

        if "PSO" in self.algoritmo:

            particulas = self.particulas.value()

            iteraciones = self.iteraciones.value()

            mejor_posicion, mejor_fitness, historial = ejecutar_pso(
                particulas,
                iteraciones
            )

            QMessageBox.information(
                self,
                "Resultado",

                f"Función: {self.funcion}\n\n"
                f"Mejor posición:\n{mejor_posicion}\n\n"
                f"Mejor fitness:\n{mejor_fitness}"
            )

        # ==========================================
        # GA
        # ==========================================

        elif "GA" in self.algoritmo:

            QMessageBox.information(
                self,
                "Información",
                "GA todavía no implementado"
            )