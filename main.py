# MAIN WINDOW FOR FITNESS APPLICATION

# LIBRARIES AND MODULES
import sys

from PyQt5.QtCore import QDate, Qt # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi 

import kuntoilija
import timetools
#TODO: Import some library able to plot trends and make it as widget in the UI graphs


# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    """MainWindow for the fitness app"""
    # Constructor
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie. buttons and input fields
        self.nameLE = self.nameLineEdit
        self.birthDateE = self.birthdayDateEdit
        self.genderCB = self.genderComboBox
        self.weighingDateE = self.weighingDateEdit

        # Set weighing date to current day
        self.weighingDateE.setDate(QDate.currentDate())
        self.heightSB = self.heightDoubleSpinBox
        self.weightSB = self.weightDoubleSpinBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self. waistSpinBox
        self.hipSB = self.hipSpinBox
        #TODO: Disable Calculate button until values have been edited
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)
        #TODO: Disable Save button until new values are calculated
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)

    # Define slots ie. methods.

    # Calculate BMI, finnish and US fat % and updates corresponding labels 
    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value()
        weight = self.weightSB.value()
        # Convert birthday data to ISO string
        birthday = self.birthDateE.date().toString(format=Qt.ISODate)
        # Set gender value according to ComboBox value
        gendertext = self.genderCB.currentText()
        if gendertext == 'Mies':
            gender = 1
        else:
            gender = 2
        # Convert weighing data to ISO string
        date_of_weighing = self.weighingDateE.date().toString(format=Qt.ISODate)
        age = timetools.date_difference(birthday, date_of_weighing, 'year')

        # Create athlete object
        athlete = kuntoilija.Kuntoilija(name, height, weight, age,gender, date_of_weighing)
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))

    #TODO: Make this method to save results to a disk drive
    # Save data to disk
    def saveData(self):
        pass


if __name__=='__main__':
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

