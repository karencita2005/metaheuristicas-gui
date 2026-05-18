import sys
from PyQt5.QtWidgets import QApplication
from interfaz.menu_principal import MenuPrincipal

app = QApplication(sys.argv)

ventana = MenuPrincipal()
ventana.show()

sys.exit(app.exec_())