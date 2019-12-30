# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartingDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartingDateLabel.setGeometry(QtCore.QRect(40, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StartingDateLabel.setFont(font)
        self.StartingDateLabel.setObjectName("StartingDateLabel")
        self.StartingDateTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.StartingDateTextbox.setGeometry(QtCore.QRect(130, 30, 101, 20))
        self.StartingDateTextbox.setText("")
        self.StartingDateTextbox.setObjectName("StartingDateTextbox")
        self.DayXLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayXLabel.setGeometry(QtCore.QRect(10, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.DayXLabel.setFont(font)
        self.DayXLabel.setObjectName("DayXLabel")
        self.TempLabel = QtWidgets.QLabel(self.centralwidget)
        self.TempLabel.setGeometry(QtCore.QRect(10, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempLabel.setFont(font)
        self.TempLabel.setObjectName("TempLabel")
        self.TempTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.TempTextbox.setGeometry(QtCore.QRect(60, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempTextbox.setFont(font)
        self.TempTextbox.setObjectName("TempTextbox")
        self.CelsiusLabel = QtWidgets.QLabel(self.centralwidget)
        self.CelsiusLabel.setGeometry(QtCore.QRect(120, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CelsiusLabel.setFont(font)
        self.CelsiusLabel.setObjectName("CelsiusLabel")
        self.MedsLabel = QtWidgets.QLabel(self.centralwidget)
        self.MedsLabel.setGeometry(QtCore.QRect(10, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.MedsLabel.setFont(font)
        self.MedsLabel.setAutoFillBackground(False)
        self.MedsLabel.setObjectName("MedsLabel")
        self.MedNameLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_1.setGeometry(QtCore.QRect(10, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_1.setFont(font)
        self.MedNameLabel_1.setObjectName("MedNameLabel_1")
        self.MedNameTextbox_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_1.setGeometry(QtCore.QRect(50, 140, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_1.setFont(font)
        self.MedNameTextbox_1.setObjectName("MedNameTextbox_1")
        self.MedDoseLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_1.setGeometry(QtCore.QRect(10, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_1.setFont(font)
        self.MedDoseLabel_1.setObjectName("MedDoseLabel_1")
        self.MedDoseTextbox_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_1.setGeometry(QtCore.QRect(50, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_1.setFont(font)
        self.MedDoseTextbox_1.setObjectName("MedDoseTextbox_1")
        self.StartMedButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_1.setGeometry(QtCore.QRect(120, 170, 71, 23))
        self.StartMedButton_1.setObjectName("StartMedButton_1")
        self.EndMedButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_1.setGeometry(QtCore.QRect(190, 170, 71, 23))
        self.EndMedButton_1.setDefault(False)
        self.EndMedButton_1.setFlat(False)
        self.EndMedButton_1.setObjectName("EndMedButton_1")
        self.AddDayButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddDayButton.setGeometry(QtCore.QRect(0, 550, 191, 101))
        self.AddDayButton.setObjectName("AddDayButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(190, 550, 81, 51))
        self.SaveButton.setObjectName("SaveButton")
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportButton.setGeometry(QtCore.QRect(190, 600, 81, 51))
        self.ExportButton.setObjectName("ExportButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 0, 561, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.LoadPatientButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadPatientButton.setEnabled(True)
        self.LoadPatientButton.setGeometry(QtCore.QRect(140, 0, 131, 23))
        self.LoadPatientButton.setObjectName("LoadPatientButton")
        self.NewPatientButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewPatientButton.setGeometry(QtCore.QRect(0, 0, 131, 23))
        self.NewPatientButton.setCheckable(False)
        self.NewPatientButton.setChecked(False)
        self.NewPatientButton.setAutoDefault(False)
        self.NewPatientButton.setDefault(False)
        self.NewPatientButton.setFlat(False)
        self.NewPatientButton.setObjectName("NewPatientButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 190, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MedDoseLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_2.setGeometry(QtCore.QRect(10, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_2.setFont(font)
        self.MedDoseLabel_2.setObjectName("MedDoseLabel_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.MedDoseTextbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_2.setGeometry(QtCore.QRect(50, 240, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_2.setFont(font)
        self.MedDoseTextbox_2.setObjectName("MedDoseTextbox_2")
        self.MedNameTextbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_2.setGeometry(QtCore.QRect(50, 210, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_2.setFont(font)
        self.MedNameTextbox_2.setObjectName("MedNameTextbox_2")
        self.MedNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_2.setGeometry(QtCore.QRect(10, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_2.setFont(font)
        self.MedNameLabel_2.setObjectName("MedNameLabel_2")
        self.StartMedButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_2.setGeometry(QtCore.QRect(120, 240, 71, 23))
        self.StartMedButton_2.setObjectName("StartMedButton_2")
        self.EndMedButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_2.setGeometry(QtCore.QRect(190, 240, 71, 23))
        self.EndMedButton_2.setDefault(False)
        self.EndMedButton_2.setFlat(False)
        self.EndMedButton_2.setObjectName("EndMedButton_2")
        self.MedDoseLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_3.setGeometry(QtCore.QRect(10, 310, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_3.setFont(font)
        self.MedDoseLabel_3.setObjectName("MedDoseLabel_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 330, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.MedDoseTextbox_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_3.setGeometry(QtCore.QRect(50, 310, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_3.setFont(font)
        self.MedDoseTextbox_3.setObjectName("MedDoseTextbox_3")
        self.MedNameTextbox_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_3.setGeometry(QtCore.QRect(50, 280, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_3.setFont(font)
        self.MedNameTextbox_3.setObjectName("MedNameTextbox_3")
        self.MedNameLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_3.setGeometry(QtCore.QRect(10, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_3.setFont(font)
        self.MedNameLabel_3.setObjectName("MedNameLabel_3")
        self.StartMedButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_3.setGeometry(QtCore.QRect(120, 310, 71, 23))
        self.StartMedButton_3.setObjectName("StartMedButton_3")
        self.EndMedButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_3.setGeometry(QtCore.QRect(190, 310, 71, 23))
        self.EndMedButton_3.setDefault(False)
        self.EndMedButton_3.setFlat(False)
        self.EndMedButton_3.setObjectName("EndMedButton_3")
        self.MedDoseLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_4.setGeometry(QtCore.QRect(10, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_4.setFont(font)
        self.MedDoseLabel_4.setObjectName("MedDoseLabel_4")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 400, 271, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.MedDoseTextbox_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_4.setGeometry(QtCore.QRect(50, 380, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_4.setFont(font)
        self.MedDoseTextbox_4.setObjectName("MedDoseTextbox_4")
        self.MedNameTextbox_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_4.setGeometry(QtCore.QRect(50, 350, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_4.setFont(font)
        self.MedNameTextbox_4.setObjectName("MedNameTextbox_4")
        self.MedNameLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_4.setGeometry(QtCore.QRect(10, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_4.setFont(font)
        self.MedNameLabel_4.setObjectName("MedNameLabel_4")
        self.StartMedButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_4.setGeometry(QtCore.QRect(120, 380, 71, 23))
        self.StartMedButton_4.setObjectName("StartMedButton_4")
        self.EndMedButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_4.setGeometry(QtCore.QRect(190, 380, 71, 23))
        self.EndMedButton_4.setDefault(False)
        self.EndMedButton_4.setFlat(False)
        self.EndMedButton_4.setObjectName("EndMedButton_4")
        self.MedDoseLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_5.setGeometry(QtCore.QRect(10, 450, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_5.setFont(font)
        self.MedDoseLabel_5.setObjectName("MedDoseLabel_5")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 470, 271, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.MedDoseTextbox_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_5.setGeometry(QtCore.QRect(50, 450, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_5.setFont(font)
        self.MedDoseTextbox_5.setObjectName("MedDoseTextbox_5")
        self.MedNameTextbox_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_5.setGeometry(QtCore.QRect(50, 420, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_5.setFont(font)
        self.MedNameTextbox_5.setObjectName("MedNameTextbox_5")
        self.MedNameLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_5.setGeometry(QtCore.QRect(10, 420, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_5.setFont(font)
        self.MedNameLabel_5.setObjectName("MedNameLabel_5")
        self.StartMedButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_5.setGeometry(QtCore.QRect(120, 450, 71, 23))
        self.StartMedButton_5.setObjectName("StartMedButton_5")
        self.EndMedButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_5.setGeometry(QtCore.QRect(190, 450, 71, 23))
        self.EndMedButton_5.setDefault(False)
        self.EndMedButton_5.setFlat(False)
        self.EndMedButton_5.setObjectName("EndMedButton_5")
        self.MedDoseLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_6.setGeometry(QtCore.QRect(10, 520, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_6.setFont(font)
        self.MedDoseLabel_6.setObjectName("MedDoseLabel_6")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 540, 271, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.MedDoseTextbox_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_6.setGeometry(QtCore.QRect(50, 520, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_6.setFont(font)
        self.MedDoseTextbox_6.setObjectName("MedDoseTextbox_6")
        self.MedNameTextbox_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_6.setGeometry(QtCore.QRect(50, 490, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_6.setFont(font)
        self.MedNameTextbox_6.setObjectName("MedNameTextbox_6")
        self.MedNameLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_6.setGeometry(QtCore.QRect(10, 490, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_6.setFont(font)
        self.MedNameLabel_6.setObjectName("MedNameLabel_6")
        self.StartMedButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.StartMedButton_6.setGeometry(QtCore.QRect(120, 520, 71, 23))
        self.StartMedButton_6.setObjectName("StartMedButton_6")
        self.EndMedButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_6.setGeometry(QtCore.QRect(190, 520, 71, 23))
        self.EndMedButton_6.setDefault(False)
        self.EndMedButton_6.setFlat(False)
        self.EndMedButton_6.setObjectName("EndMedButton_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(260, 0, 20, 651))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Diagram Maker"))
        self.StartingDateLabel.setText(_translate("MainWindow", "Starting Date:"))
        self.DayXLabel.setText(_translate("MainWindow", "Day 1"))
        self.TempLabel.setText(_translate("MainWindow", "Temp:"))
        self.CelsiusLabel.setText(_translate("MainWindow", "°C"))
        self.MedsLabel.setText(_translate("MainWindow", "Meds"))
        self.MedNameLabel_1.setText(_translate("MainWindow", "Name:"))
        self.MedDoseLabel_1.setText(_translate("MainWindow", "Dose:"))
        self.StartMedButton_1.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_1.setText(_translate("MainWindow", "End"))
        self.AddDayButton.setText(_translate("MainWindow", "Add Day"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.LoadPatientButton.setText(_translate("MainWindow", "Load"))
        self.NewPatientButton.setText(_translate("MainWindow", "New"))
        self.MedDoseLabel_2.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_2.setText(_translate("MainWindow", "Name:"))
        self.StartMedButton_2.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_2.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_3.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_3.setText(_translate("MainWindow", "Name:"))
        self.StartMedButton_3.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_3.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_4.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_4.setText(_translate("MainWindow", "Name:"))
        self.StartMedButton_4.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_4.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_5.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_5.setText(_translate("MainWindow", "Name:"))
        self.StartMedButton_5.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_5.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_6.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_6.setText(_translate("MainWindow", "Name:"))
        self.StartMedButton_6.setText(_translate("MainWindow", "Start"))
        self.EndMedButton_6.setText(_translate("MainWindow", "End"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
