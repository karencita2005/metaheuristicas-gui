from PyQt5.QtWidgets import *
from algoritmos.pso import ejecutar_pso

class VentanaConfiguracion(QWidget):

    def __init__(self, problema, algoritmo, objetivo):
        super().__init__()

        # ==========================================
        # GUARDAR DATOS
        # ==========================================

        self.algoritmo = algoritmo

        # ==========================================
        # CONFIGURACIÓN DE VENTANA
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
        # INFORMACIÓN SELECCIONADA
        # ==========================================

        layout.addWidget(QLabel(f"Problema: {problema}"))
        layout.addWidget(QLabel(f"Algoritmo: {algoritmo}"))
        layout.addWidget(QLabel(f"Objetivo: {objetivo}"))

        # ==========================================
        # CONFIGURACIÓN PSO
        # ==========================================

        if "PSO" in algoritmo:

            # Número de partículas
            self.particulas = QSpinBox()
            self.particulas.setValue(30)

            layout.addWidget(QLabel("Número de partículas"))
            layout.addWidget(self.particulas)

            # Número de iteraciones
            self.iteraciones = QSpinBox()
            self.iteraciones.setValue(100)

            layout.addWidget(QLabel("Número de iteraciones"))
            layout.addWidget(self.iteraciones)

        # ==========================================
        # CONFIGURACIÓN GA
        # ==========================================

        elif "GA" in algoritmo:

            # Tamaño población
            self.poblacion = QSpinBox()
            self.poblacion.setValue(50)

            layout.addWidget(QLabel("Tamaño de población"))
            layout.addWidget(self.poblacion)

            # Generaciones
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
    # FUNCIÓN EJECUTAR ALGORITMO
    # ==========================================

    def ejecutarAlgoritmo(self):

        # ==========================================
        # EJECUTAR PSO
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

                f"Mejor posición:\n{mejor_posicion}\n\n"
                f"Mejor fitness:\n{mejor_fitness}"
            )

        # ==========================================
        # GA TEMPORAL
        # ==========================================

        elif "GA" in self.algoritmo:

            QMessageBox.information(
                self,
                "Información",
                "GA todavía no implementado"
            )