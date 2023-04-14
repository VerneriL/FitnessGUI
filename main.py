# MAIN WINDOW FOR FITNESS APPLICATION

# LIBRARIES AND MODULES
import sys

from PyQt5.QtCore import QDate, Qt # Core functionality of Qt
from PyQt5 import QtCore
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

        self.nameLE = self.findChild(QtWidgets.QLineEdit, 'nameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)
        # Define UI Controls ie. buttons and input fields
        self.birthDateE = self.birthdayDateEdit
        self.birthDateE.dateChanged.connect(self.activateCalculatePB)
        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)
        self.weighingDateE = self.weighingDateEdit

        # Set weighing date to current day
        self.weighingDateE.setDate(QDate.currentDate())
        self.heightSB = self.heightDoubleSpinBox
        self.heightSB.valueChanged.connect(self.activateCalculatePB)
        self.weightSB = self.weightDoubleSpinBox
        self.weightSB.valueChanged.connect(self.activateCalculatePB)
        self.neckSB = self.neckSpinBox
        self.neckSB.valueChanged.connect(self.activateCalculatePB)
        self.waistSB = self. waistSpinBox
        self.waistSB.valueChanged.connect(self.activateCalculatePB)
        self.hipSB = self.hipSpinBox
        self.hipSB.setEnabled(False)
        self.hipSB.valueChanged.connect(self.activateCalculatePB)
        #TODO: Disable Calculate button until values have been edited
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)
        #TODO: Disable Save button until new values are calculated
        self.savePB = self.findChild(QtWidgets.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)

    # Define slots ie. methods.

    def activateCalculatePB(self):
        self.calculatePB.setEnabled(True)
        if self.nameLE.text() == '':
            self.calculatePB.setEnabled(False)
        if self.birthDateE.date() == QtCore.QDate(1900, 1, 1):
            self.calculatePB.setEnabled(False)
        if self.genderCB.currentTest() == '':
            self.genderCB.setEnabled(False)
        if self.heightSB.value() == 100:
            self.calculatePB.setEnabled(False)
        if self.weight.value() == 20:
            self.calculatePB.setEnabled(False)
        if self.neckSB.value() == 10:
            self.calculatePB.setEnabled(False)
        if self.waistSB.value() == 30:
            self.calculatePB.setEnabled(False)
        if self.gender.currentText() == 'Nainen':
            self.hipSB.setEnabled(True)
            if self.hipSB.value() == 50:
                self.calculatePB.setEnabled(False)
        else:
            self.hipSB.setEnabled(False)

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
            gender = 0
        # Convert weighing data to ISO string
        date_of_weighing = self.weighingDateE.date().toString(format=Qt.ISODate)
        age = timetools.date_difference(birthday, date_of_weighing, 'year')

        neck = self.neckSB.value()
        waist = self.waistSB.value()
        hip = self.hipSB.value()

        # Create athlete object
        if age >= 18:
            athlete = kuntoilija.Kuntoilija(name, height, weight, age,gender, date_of_weighing)
        else:
            athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date_of_weighing)
        bmi = athlete.bmi
        self.bmiLabel.setText(str(bmi))
        
        fiFatPercentage = athlete.rasvaprosentti

        if gender == 1:
            usaFatPercentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
        else:
            usaFatPercentage = athlete.usa_rasvaprosentti_nainen(height, waist, hip, neck)

        # Set fat percentages
        self.fatFiLabel.setText(str(fiFatPercentage))
        self.fatUsLabel.setText(str(usaFatPercentage))

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

