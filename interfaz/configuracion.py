from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Importación corregida apuntando a la carpeta utils
from utils.graficas import VentanaGrafica

from algoritmos.pso import ejecutar_pso
from algoritmos.ga import ejecutar_ga

from problemas.continuas import *
from problemas.binarias import *
from problemas.categoricas import *


class VentanaConfiguracion(QWidget):

    def __init__(self, problema, funcion, algoritmo, objetivo):
        super().__init__()

        self.problema = problema
        self.funcion = funcion
        self.algoritmo = algoritmo
        self.objetivo = objetivo

        # Inputs inicializados en None por seguridad
        self.particulas = None
        self.iteraciones = None
        self.poblacion = None
        self.generaciones = None
        self.mutacion = None
        self.cruza = None
        self.dimensiones = None

        self.setWindowTitle("Configuración del Algoritmo")
        self.resize(450, 500)

        layout_principal = QVBoxLayout()
        layout_form = QFormLayout()

        titulo = QLabel("Configuración de Parámetros")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(titulo)

        layout_form.addRow("<b>Problema seleccionado:</b>", QLabel(problema))
        layout_form.addRow("<b>Función objetivo:</b>", QLabel(funcion))
        layout_form.addRow("<b>Algoritmo a ejecutar:</b>", QLabel(algoritmo))
        layout_form.addRow("<b>Estrategia:</b>", QLabel(objetivo))
        
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)
        layout_form.addRow(separador)

        # Renderizado de campos según el algoritmo
        if "PSO" in algoritmo:
            self.particulas = QSpinBox()
            self.particulas.setRange(1, 1000)
            self.particulas.setValue(30)
            layout_form.addRow("Número de partículas:", self.particulas)

            self.iteraciones = QSpinBox()
            self.iteraciones.setRange(1, 10000)
            self.iteraciones.setValue(100)
            layout_form.addRow("Número de iteraciones:", self.iteraciones)

            self.dimensiones = QSpinBox()
            self.dimensiones.setRange(2, 100)
            self.dimensiones.setValue(2)
            layout_form.addRow("Dimensiones del problema:", self.dimensiones)

        elif "GA" in algoritmo:
            self.poblacion = QSpinBox()
            self.poblacion.setRange(2, 1000)
            self.poblacion.setValue(50)
            layout_form.addRow("Tamaño de población:", self.poblacion)

            self.generaciones = QSpinBox()
            self.generaciones.setRange(1, 10000)
            self.generaciones.setValue(100)
            layout_form.addRow("Número de generaciones:", self.generaciones)

            self.mutacion = QDoubleSpinBox()
            self.mutacion.setRange(0.0, 1.0)
            self.mutacion.setSingleStep(0.01)
            self.mutacion.setValue(0.10)
            layout_form.addRow("Tasa de mutación:", self.mutacion)

            self.cruza = QDoubleSpinBox()
            self.cruza.setRange(0.0, 1.0)
            self.cruza.setSingleStep(0.01)
            self.cruza.setValue(0.80)
            layout_form.addRow("Tasa de cruza:", self.cruza)

            self.dimensiones = QSpinBox()
            self.dimensiones.setRange(2, 100)
            self.dimensiones.setValue(10)
            layout_form.addRow("Dimensiones del problema:", self.dimensiones)

        layout_principal.addLayout(layout_form)
        layout_principal.addStretch()

        boton_ejecutar = QPushButton("Ejecutar")
        boton_ejecutar.setStyleSheet("padding: 10px; font-size: 14px; font-weight: bold;")
        boton_ejecutar.clicked.connect(self.ejecutarAlgoritmo)
        layout_principal.addWidget(boton_ejecutar)

        self.setLayout(layout_principal)

    def obtenerFuncion(self):
        funciones = {
            "Sphere": sphere, "Rastrigin": rastrigin, "Rosenbrock": rosenbrock,
            "OneMax": onemax, "Binario Inverso": binario_inverso, "Color Matching": color_matching
        }
        return funciones.get(self.funcion, None)

    def ejecutarAlgoritmo(self):
        funcion = self.obtenerFuncion()
        if not funcion:
            QMessageBox.critical(self, "Error", f"La función '{self.funcion}' no está mapeada.")
            return

        self.ventana_grafica = None

        # Ejecución PSO
        if "PSO" in self.algoritmo and self.particulas:
            particulas = self.particulas.value()
            iteraciones = self.iteraciones.value()
            dimensiones = self.dimensiones.value()

            # LÍNEA 131 CORREGIDA:
            mejor, fitness, historial = ejecutar_pso(funcion, particulas, iteraciones, dimensiones=dimensiones)
            QMessageBox.information(
                self, "Resultado PSO",
                f"<b>Mejor posición encontrada:</b><br>{mejor}<br><br>"
                f"<b>Fitness óptimo:</b><br>{fitness}<br><br>"
                f"<b>Iteraciones completadas:</b><br>{len(historial)}"
            )
            
            self.ventana_grafica = VentanaGrafica(historial, self.algoritmo, self.funcion, self.objetivo, self)
            self.ventana_grafica.show()

        # Ejecución GA
        elif "GA" in self.algoritmo and self.poblacion:
            poblacion = self.poblacion.value()
            generaciones = self.generaciones.value()
            tasa_mutacion = self.mutacion.value()
            tasa_cruza = self.cruza.value()
            dimensions = self.dimensiones.value()

            objetivo = "max" if "Max" in self.objetivo else "min"
            tipo = "binario" if "binaria" in self.problema.lower() else "continuo"

            mejor, fitness, historial = ejecutar_ga(
                funcion, poblacion, generaciones, tasa_mutacion, tasa_cruza, objetivo, tipo, dimensions
            )

            QMessageBox.information(
                self, "Resultado GA",
                f"<b>Mejor solución encontrada:</b><br>{mejor}<br><br>"
                f"<b>Fitness óptimo:</b><br>{fitness}<br><br>"
                f"<b>Generaciones ejecutadas:</b><br>{len(historial)}"
            )
            
            self.ventana_grafica = VentanaGrafica(historial, self.algoritmo, self.funcion, self.objetivo, self)
            self.ventana_grafica.show()

        elif any(alg in self.algoritmo for alg in ["ACO", "AIS", "DE"]):
            QMessageBox.information(self, "Módulo Incompleto", f"El algoritmo {self.algoritmo} se encuentra en desarrollo.")