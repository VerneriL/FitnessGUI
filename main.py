# MAIN WINDOW FOR FITNESS APPLICATION

# LIBRARIES AND MODULES
import sys

from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi 



# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    """MainWindow for the fitness app"""

    # Constructor
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie. buttons and input fields
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)

    # Define slots ie. methods.
    def calculateAll(self):
        self.bmiLabel.setText('100')

if __name__=='__main__':
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

