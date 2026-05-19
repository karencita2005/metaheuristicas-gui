import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class VentanaGrafica(QDialog):
    def __init__(self, historial, nombre_algoritmo, nombre_funcion, objetivo, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle(f"Análisis de Convergencia - {nombre_algoritmo}")
        self.resize(600, 450)
        
        layout = QVBoxLayout()
        
        info_label = QLabel(
            f"<b>Algoritmo:</b> {nombre_algoritmo} | "
            f"<b>Función:</b> {nombre_funcion}<br>"
            f"<b>Estrategia:</b> {objetivo} | "
            f"<b>Óptimo Final:</b> {historial[-1]:.6f}"
        )
        info_label.setStyleSheet("font-size: 13px; margin-bottom: 10px;")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)
        
        # Crear la gráfica
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        
        # Dibujar los datos
        self.graficar_convergencia(historial, nombre_algoritmo)
        
        boton_cerrar = QPushButton("Cerrar Gráfica")
        boton_cerrar.setStyleSheet("padding: 8px; font-weight: bold;")
        boton_cerrar.clicked.connect(self.close)
        layout.addWidget(boton_cerrar)
        
        self.setLayout(layout)

    def graficar_convergencia(self, historial, algoritmo):
        self.ax.clear()
        color = "purple" if "PSO" in algoritmo else "blue"
        
        self.ax.plot(historial, label="Mejor Fitness", color=color, linewidth=2)
        self.ax.set_title("Curva de Convergencia Evolutiva", fontsize=12, fontweight='bold')
        self.ax.set_xlabel("Iteración / Generación", fontsize=10)
        self.ax.set_ylabel("Valor de Fitness (Aptitud)", fontsize=10)
        self.ax.grid(True, linestyle="--", alpha=0.6)
        self.ax.legend()
        
        self.fig.tight_layout()
        self.canvas.draw()