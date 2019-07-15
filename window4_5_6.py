from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDialog
from PyQt5.QtWidgets import QTextEdit, QPushButton,QMessageBox, QAction, qApp
from PyQt5.QtGui import QFont
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from Database import database
import Edit


class window4(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui_win4()

    def init_ui_win4(self):

        self.setStyleSheet(" colour: black ; font-size: 13pt ; font-family: arial")

        self.enr = QLineEdit(self)

        self.lenr = QLabel(self)
        self.lenr.setText('ENTER ENROLLMENT NO:')

        self.edt_pers = QPushButton('EDIT PERSONAL INFORMATION',self)
        self.edt_acd = QPushButton('EDIT ACADEMIC INFORMATION',self)

        self.edt_pers.setStyleSheet("background:teal; color: yellow ; font-size: 13pt ; font-family: arial")
        self.edt_acd.setStyleSheet("background:teal; color: yellow; font-size: 13pt ; font-family: arial")

        layout_win4 = QGridLayout(self)
        layout_win4.addWidget(self. lenr, 1, 1)
        layout_win4.addWidget(self.enr, 1, 2)
        layout_win4.addWidget(self.edt_pers, 2, 1, 1, 2)
        layout_win4.addWidget(self.edt_acd, 3, 1, 1, 2)

        title="EDIT DATA WINDOW"
        self.resize(350,100)

        self.edt_acd.clicked.connect(self.edt_academic)
        self.edt_pers.clicked.connect(self.edt_personal)

        self.setWindowTitle(title)
        self.show()

    def edt_personal(self):
        self.edtpers = Edit.EditPersonal("'" + self.enr.text() + "'")
        self.accept()

    def edt_academic(self):
        self.edtacad = Edit.EditAcademic("'" + self.enr.text() + "'")
        self.accept()

class window5(database, QDialog):

    def __init__(self):
        database.__init__(self)
        QDialog.__init__(self)
        self.init_ui_win5()

    def init_ui_win5(self):
        self.setStyleSheet(" colour: black ; font-size: 13pt ; font-family: arial")

        ##lienedit and label for enrollement no
        self.enr = QLineEdit(self)
        self.lenr = QLabel(self)
        self.lenr.setText('ENTER ENROLLMENT NO:')

        ##lieedit and label for attendance
        self.att = QLineEdit(self)
        self.latt = QLabel(self)
        self.latt.setText('ENTER ATTENDENCE:')

        self.sub_att = QPushButton('SUBMIT ATTENDENCE', self)
        self.sub_att.setStyleSheet("background:teal; colour:yellow ; font-size: 13pt ; font-family: arial")

        layout_win5 = QGridLayout(self)
        layout_win5.addWidget(self.lenr, 1, 1)
        layout_win5.addWidget(self.enr, 1, 2)

        layout_win5.addWidget(self.latt, 2,1 )
        layout_win5.addWidget(self.att, 2, 2)

        layout_win5.addWidget(self.sub_att, 3, 1, 1, 2)


        title="Enter Attendence"
        self.resize(400,150)

        self.sub_att.clicked.connect(self.updt)

        self.setWindowTitle(title)
        self.show()

    def updt(self):
        QMessageBox.information(self, 'Successful', 'Attendance has been updated for enroll ' + self.enr.text())
        self.update_attendance(self.enr.text(), float(self.att.text()))
        self.accept()


class window6(database, QDialog):
    def __init__(self):
        database.__init__(self)
        QDialog.__init__(self)
        self.init_ui_win6()

    def init_ui_win6(self):
        self.setStyleSheet("color: black ; font-size: 13pt ; font-family: arial")

        ##lienedit and label for enrollement no
        self.enr = QLineEdit(self)
        self.lenr = QLabel(self)
        self.lenr.setText('ENTER ENROLLMENT NO:')

        ##lieedit and label for attendance
        self.cgpa = QLineEdit(self)
        self.lcgpa = QLabel(self)
        self.lcgpa.setText('ENTER CGPA:')

        self.sub_cgpa = QPushButton('SUBMIT CGPA', self)
        self.sub_cgpa.setStyleSheet("background:teal; color: yellow ; font-size: 13pt ; font-family: arial")

        layout_win6 = QGridLayout(self)
        layout_win6.addWidget(self.lenr, 1, 1)
        layout_win6.addWidget(self.enr, 1, 2)

        layout_win6.addWidget(self.lcgpa, 2,1 )
        layout_win6.addWidget(self.cgpa, 2, 2)

        layout_win6.addWidget(self.sub_cgpa, 3, 1, 1, 2)

        title="Enter CGPA"
        self.resize(400,150)

        self.sub_cgpa.clicked.connect(self.updt)

        self.setWindowTitle(title)
        self.show()

    def updt(self):
        self.update_gpa(float(self.cgpa.text()),self.enr.text())
        QMessageBox.information(self, 'Successful', 'CGPA has been updated for enroll ' + self.enr.text())
        self.accept()