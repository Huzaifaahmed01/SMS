from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, \
    QDialog
from PyQt5.QtWidgets import QTextEdit, QPushButton, QAction, qApp, QMessageBox
from PyQt5.QtGui import QFont
from Database import database
import sys

print('student management system')


class window2(database, QDialog):
    def __init__(self):
        database.__init__(self)
        QDialog.__init__(self)

    def init_ui(self, personal_info):
        self.setStyleSheet("font-size: 13pt ; font-family: arial")
        self.resize(400, 200)

        ##textBoxes defined
        self.enroll = QLineEdit(self)
        self.roll = QLineEdit(self)
        self.dept = QLineEdit(self)
        self.batch = QLineEdit(self)
        self.attend = QLineEdit(self)
        self.cgpa = QLineEdit(self)

        ##pushbutton defined
        self.submit = QPushButton(self)
        self.reset_win2 = QPushButton(self)

        ##setting text to buttons
        self.submit.setText('Submit')
        self.reset_win2.setText('Reset')

        ##label defined
        self.lenroll = QLabel(self)
        self.lroll = QLabel(self)
        self.lsec = QLabel(self)
        self.ldept = QLabel(self)
        self.lbatch = QLabel(self)
        self.lshift = QLabel(self)
        self.lattend = QLabel(self)
        self.lyr = QLabel(self)
        self.lcgpa = QLabel(self)

        ##label set text
        self.lenroll.setText('EnRoll no:')
        self.lroll.setText('Roll no:')
        self.lsec.setText('Section:')
        self.ldept.setText('Department:')
        self.lbatch.setText('Batch:')
        self.lshift.setText('Shift:')
        self.lattend.setText('Attendance:')
        self.lyr.setText('year:')
        self.lcgpa.setText('CGPA:')

        # label font setting
        labelfont = QFont('times', 14)
        self.lenroll.setFont(labelfont)
        self.lroll.setFont(labelfont)
        self.lsec.setFont(labelfont)
        self.lshift.setFont(labelfont)
        self.ldept.setFont(labelfont)
        self.lbatch.setFont(labelfont)
        self.lattend.setFont(labelfont)
        self.lyr.setFont(labelfont)
        self.lcgpa.setFont(labelfont)

        self.sec = QComboBox(self)
        self.sec.addItem("A")
        self.sec.addItem("B")
        self.sec.addItem("C")
        self.sec.addItem("D")

        self.shift = QComboBox(self)
        self.shift.addItem("Morning")
        self.shift.addItem("Evening")

        self.year = QComboBox(self)
        self.year.addItem("First year")
        self.year.addItem("Second  year")
        self.year.addItem("Third year")
        self.year.addItem("Final year")

        self.Grid_win = QGridLayout(self)
        self.Grid_win.addWidget(self.lenroll, 1, 1)
        self.Grid_win.addWidget(self.lroll, 2, 1)
        self.Grid_win.addWidget(self.lsec, 3, 1)
        self.Grid_win.addWidget(self.ldept, 4, 1)
        self.Grid_win.addWidget(self.lbatch, 5, 1)
        self.Grid_win.addWidget(self.lshift, 6, 1)
        self.Grid_win.addWidget(self.lyr, 7, 1)
        self.Grid_win.addWidget(self.lattend, 8, 1)
        self.Grid_win.addWidget(self.lcgpa, 9, 1)

        self.Grid_win.addWidget(self.enroll, 1, 2)
        self.Grid_win.addWidget(self.roll, 2, 2)
        self.Grid_win.addWidget(self.sec, 3, 2)
        self.Grid_win.addWidget(self.dept, 4, 2)
        self.Grid_win.addWidget(self.batch, 5, 2)
        self.Grid_win.addWidget(self.shift, 6, 2)
        self.Grid_win.addWidget(self.year, 7, 2)
        self.Grid_win.addWidget(self.attend, 8, 2)
        self.Grid_win.addWidget(self.cgpa, 9, 2)

        self.Grid_win.addWidget(self.submit, 10, 1)
        self.Grid_win.addWidget(self.reset_win2, 10, 2)

        #connect to function
        self.submit.clicked.connect(lambda: self.submit_func(personal_info))
        self.reset_win2.clicked.connect(self.reset_win2_func)

        self.setWindowTitle('student management system')

        self.show()

    def submit_func(self, per):
        if self.enroll.text()=='' or self.roll.text()=='' or self.dept.text()=='' or self.batch.text()=='' or self.attend.text()=='' or self.cgpa.text() == '':
            QMessageBox.warning(self, 'Error', 'Fields is/are left to fill')
        elif enrollment(self.enroll.text()) == False:
            QMessageBox.warning(self, 'Error', 'Enrollment entered is wrong')
        elif float(self.cgpa.text())>4.0:
            QMessageBox.warning(self, 'Error', 'CGPA must not exceed 4.0')
        elif float(self.attend.text())>100:
            QMessageBox.warning(self, 'Error', 'Attendance must not exceed 100')
        else:
            self.personallist = per
            acad = self.enroll.text() + '|' + self.roll.text() + '|' + str(self.sec.currentIndex()) + '|' +self.dept.text() + '|' +self.batch.text() + '|' +str(self.shift.currentIndex()) + '|' +str(self.year.currentIndex()) + '|' +self.attend.text() + '|' +self.cgpa.text()
            self.academiclist = acad.split('|')
            self.enter_database(self.personallist,self.academiclist)
            QMessageBox.information(self, 'Successful', 'Student is added successfully to the database.')
            self.accept()


    def reset_win2_func(self):
        self.enroll.clear()
        self.roll.clear()
        self.dept.clear()
        self.batch.clear()
        self.attend.clear()
        self.cgpa.clear()


def enrollment(enr):
    if enr[:2].isalpha() and enr[3:].isdigit():
        return True
    else:
        return False

if __name__=="__main__":
    App=QApplication(sys.argv)
    window=window2()
    sys.exit(App.exec())