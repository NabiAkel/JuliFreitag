from PyQt6.QtWidgets import QMainWindow
from ChartView import ChartView


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = ChartView(parent)

        #self.setMinimumWidt()
        #self.setMaximumHeight()

        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Einführung in QCharts")