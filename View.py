from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDialog
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from Database import database

class view_data(database, QDialog):
    def __init__(self, enroll):
        database.__init__(self)
        QDialog.__init__(self)

        self.enr = enroll

        self.latt2 = QLabel(self)
        self.lcgpa2 = QLabel(self)

        self.c.execute("SELECT attendance, cgpa FROM academic_info WHERE enrollment_number ="+enroll)
        data = self.c.fetchone()

        self.init_ui()

        self.latt2.setText(str(data[0]))
        self.lcgpa2.setText(str(data[1]))

    def init_ui(self):
        self.setStyleSheet("color: black ; font-size: 13pt ; font-family: arial")

        self.latt = QLabel(self)
        self.latt.setText('ATTENDENCE:')

        self.lcgpa = QLabel(self)
        self.lcgpa.setText('CGPA:')

        self.view_pers = QPushButton('view PERSONAL INFORMATION',self)
        self.view_acad = QPushButton('view ACADEMIC INFORMATION',self)

        self.view_pers.setStyleSheet("background:teal; color: yellow ; font-size: 13pt ; font-family: arial")
        self.view_acad.setStyleSheet("background:teal; color: yellow; font-size: 13pt ; font-family: arial")

        layout = QGridLayout(self)
        layout.addWidget(self. latt, 3, 1)
        layout.addWidget(self.latt2, 3, 2)
        layout.addWidget(self.lcgpa2, 4, 2)
        layout.addWidget(self.lcgpa, 4, 1)
        layout.addWidget(self.view_pers, 1, 1, 1, 2)
        layout.addWidget(self.view_acad, 2, 1, 1, 2)

        title="View DATA WINDOW"
        self.resize(350,100)

        self.setWindowTitle(title)

        self.view_acad.clicked.connect(self.viewacad)
        self.view_pers.clicked.connect(self.viewpers)

        self.show()

    def viewpers(self):
        self.view_personal_info(self.enr)
        table1_view(self.personal_list)

    def viewacad(self):
        self.view_academic_info(self.enr)
        table2_view(self.academic_list)


def table1_view(lst):
    gender = ''
    religion = ''
    if lst[6] == 0:
        gender = 'Male'
    elif lst[6] == 1:
        gender = 'Female'

    if lst[8] == 0:
        religion = 'Islam'
    elif lst[8] == 1:
        religion = 'Christianity'
    elif lst[8] == 2:
        religion = 'Hinduism'
    elif lst[8] == 3:
        religion = 'Judaism'

    table = QTableWidget()
    tableItem = QTableWidgetItem()
    table.setWindowTitle("Student Details")
    table.setRowCount(14)
    table.setColumnCount(2)

    perslst = ['Student Name','Student CNIC/B-form','Fathers Name','Fathers CNIC','Date Of Birth','Gender',
               'Permenant Address','Religion','Nationality', 'Country','City','Email Address', 'Mobile No',
               'Telephone No','Residence']
    for i in range(1, 15):
        table.setItem(i-1, 0, QTableWidgetItem(perslst[i-1]))
        if i-1 == 5:
            table.setItem(i-1, 1, QTableWidgetItem(gender))
        elif i-1 == 7:
            table.setItem(i-1, 1, QTableWidgetItem(religion))
        else:
            table.setItem(i-1, 1, QTableWidgetItem(str(lst[i])))
    table.show()
    dialog = QDialog()
    dialog.setWindowTitle("Student Academic Details")
    dialog.resize(270, 400)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()

def table2_view(lst):
    Section = ''
    Shift = ''
    year = ''

    if lst[2] == 0:
        Section = 'A'
    elif lst[2] == 1:
        Section = 'B'
    elif lst[2] == 2:
        Section = 'C'
    elif lst[2] == 3:
        Section = 'D'

    if lst[5] == 0:
        Shift = 'Morning'
    elif lst[5] == 1:
        Shift = 'Evening'

    if lst[6] == 0:
        year = 'FE'
    elif lst[6] == 1:
        year = 'SE'
    elif lst[6] == 2:
        year = 'TE'
    elif lst[6] == 3:
        year = 'BE'

    table = QTableWidget()
    tableItem = QTableWidgetItem()
    table.setWindowTitle("Student Details")
    table.setRowCount(9)
    table.setColumnCount(2)
    acadlst = ['Enroll no', 'Roll no', 'Section', 'Department', 'Batch', 'Shift', 'Attendance', 'Year', 'CGPA']
    for i in range(0, 9):
        table.setItem(i, 0, QTableWidgetItem(acadlst[i]))
        if i == 2:
            table.setItem(i, 1, QTableWidgetItem(Section))
        elif i == 5:
            table.setItem(i, 1, QTableWidgetItem(Shift))
        elif i == 6:
            table.setItem(i, 1, QTableWidgetItem(year))
        else:
            table.setItem(i, 1, QTableWidgetItem(str(lst[i])))
    table.show()
    dialog = QDialog()
    dialog.setWindowTitle("Student Academic Details")
    dialog.resize(242, 320)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()


if __name__=='__main__':
    App=QApplication(sys.argv)
    window=view_data("'cs-12349'")
    sys.exit(App.exec())