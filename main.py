import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow


app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec())