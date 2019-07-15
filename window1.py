import sys,sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget,QPushButton,QApplication,QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QDialog,QApplication,QMainWindow,QWidget,QTableWidgetItem,QTableWidget,QCheckBox,QGridLayout,QGroupBox,QMenu,QPushButton,QRadioButton, QVBoxLayout,QWidget,QLabel,QLineEdit,QHBoxLayout)
from window2 import window2
import window3
print('STUDENT MODULE')

class window1(QDialog):
    def __init__(self, next):
        super().__init__()
        self.next_window = next
        self.init_ui()

    def init_ui(self):

        self.setStyleSheet("font-size: 13pt ; font-family: arial")

        self.resize(700, 500)

        # PushButtons Defined
        self.next = QPushButton(self)
        self.reset = QPushButton(self)

        # textBoxes defined
        self.Fname = QLineEdit(self)
        self.c1 = QLineEdit(self)
        self.Ftname = QLineEdit(self)
        self.c2 = QLineEdit(self)
        self.dob = QLineEdit(self)
        self.Add = QLineEdit(self)
        self.Na = QLineEdit(self)
        self.count = QLineEdit(self)
        self.city = QLineEdit(self)
        self.Email = QLineEdit(self)
        self.mob = QLineEdit(self)
        self.Tel = QLineEdit(self)
        self.res=QLineEdit(self)

        # label defined
        self.lFname = QLabel(self)
        self.lc1 = QLabel(self)
        self.lFtname = QLabel(self)
        self.lc2 = QLabel(self)
        self.ldob = QLabel(self)
        self.lg = QLabel(self)
        self.lAdd = QLabel(self)
        self.lRe = QLabel(self)
        self.lNa = QLabel(self)
        self.lcount = QLabel(self)
        self.lcity = QLabel(self)
        self.lEmail = QLabel(self)
        self.lmob = QLabel(self)
        self.lTel = QLabel(self)
        self.lres=QLabel(self)

        # label set text
        self.lFname.setText('Student Name:')
        self.lc1.setText('Student CNIC/B-form:')
        self.lFtname.setText('Fathers Name:')
        self.lc2.setText('Fathers CNIC:')
        self.ldob.setText('Date Of Birth:')
        self.lg.setText('Gender:')
        self.lAdd.setText('Permenant Address:')
        self.lRe.setText('Religion:')
        self.lNa.setText('Nationality:')
        self.lcount.setText('Country:')
        self.lcity.setText('City:')
        self.lEmail.setText('Email Adress:')
        self.lmob.setText('Mobile No:')
        self.lTel.setText('Telephone No:')
        self.lres.setText('Residence:')

        # setting text of buttons
        self.next.setText('Next')
        self.reset.setText('Reset')

        # ComboBox i.e Drop down menus
        self.g = QComboBox(self)
        self.g.addItem("Male")
        self.g.addItem("Female")
        self.Re=QComboBox(self)
        self.Re.addItem('Islam')
        self.Re.addItem('Christianity')
        self.Re.addItem('Hinduism')
        self.Re.addItem('Judaism')

        #Setting Grid Layout
        self.Grid = QGridLayout(self)
        self.Grid.addWidget(self.lFname, 1, 1)
        self.Grid.addWidget(self.lc1, 2, 1)
        self.Grid.addWidget(self.lFtname,3,1)
        self.Grid.addWidget(self.lc2,4,1)
        self.Grid.addWidget(self.ldob,5,1)
        self.Grid.addWidget(self.lg,6,1)
        self.Grid.addWidget(self.lAdd,7,1)
        self.Grid.addWidget(self.lRe,8,1)
        self.Grid.addWidget(self.lNa,9,1)
        self.Grid.addWidget(self.lcount,10,1)
        self.Grid.addWidget(self.lcity,11,1)
        self.Grid.addWidget(self.lEmail,12,1)
        self.Grid.addWidget(self.lmob,13,1)
        self.Grid.addWidget(self.lTel,14,1)
        self.Grid.addWidget(self.lres,15,1)

        self.Grid.addWidget(self.Fname, 1, 2)
        self.Grid.addWidget(self.c1, 2, 2)
        self.Grid.addWidget(self.Ftname,3,2)
        self.Grid.addWidget(self.c2,4,2)
        self.Grid.addWidget(self.dob,5,2)
        self.Grid.addWidget(self.g,6,2)
        self.Grid.addWidget(self.Add,7,2)
        self.Grid.addWidget(self.Re,8,2)
        self.Grid.addWidget(self.Na,9,2)
        self.Grid.addWidget(self.count,10,2)
        self.Grid.addWidget(self.city,11,2)
        self.Grid.addWidget(self.Email,12,2)
        self.Grid.addWidget(self.mob,13,2)
        self.Grid.addWidget(self.Tel,14,2)
        self.Grid.addWidget(self.res,15,2)

        self.Grid.addWidget(self.reset, 16, 1)
        self.Grid.addWidget(self.next, 16, 2)

        # function map to button click
        self.next.clicked.connect(self.next_func)
        self.reset.clicked.connect(self.reset_func)

        # title
        self.setWindowTitle('STUDENT MODULE')

        self.show()

    def next_func(self):
        if 	self.Fname.text() == '' or self.c1.text() == '' or self.Ftname.text() == '' or self.c2.text() == '' or \
                self.dob.text() == '' or self.Add.text() == '' or self.Na.text() == '' or self.count.text() == '' or\
                self.city.text() == '' or self.Email.text() == '' or self.mob.text() == '' or self.Tel.text() == '' or\
                self.res.text() == '':
            QMessageBox.warning(self, 'Error', 'Fields is/are left to fill')
        elif (len(self.mob.text())==11 or len(self.mob.text())==13)is False:
            print(len(self.mob.text()))
            QMessageBox.warning(self, 'Error', 'Mobile Number entered is incorrect')
        elif (len(self.c1.text()) == 13 and len(self.c2.text()) == 13) is False:
            print(len(self.c1.text()))
            print(len(self.c2.text()))
            QMessageBox.warning(self, 'Error', 'CNIC Number entered is incorrect')
        elif (checkemail(self.Email.text()) == 2)is False:
            print(checkemail(self.Email.text()))
            QMessageBox.warning(self, 'Error', 'Email entered is incorrect')
        else:
            string = self.Fname.text() + "|" + self.c1.text() + "|" + self.Ftname.text() + "|" + self.c2.text() + "|" + self.dob.text() + "|" + str(self.g.currentIndex()) + "|" + self.Add.text() + "|" + str(self.Re.currentIndex()) + "|" + self.Na.text() + "|" + self.count.text() + "|" + self.city.text() + "|" + self.Email.text() + "|" + self.mob.text() + "|" + self.Tel.text() + "|" + self.res.text()
            st = string.split('|')
            self.next_window.init_ui(st)
            self.next_window.show()
            self.accept()

    def reset_func(self):
        self.Fname.clear()
        self.c1.clear()
        self.Ftname.clear()
        self.c2.clear()
        self.dob.clear()
        self.Add.clear()
        self.Na.clear()
        self.count.clear()
        self.city.clear()
        self.Email.clear()
        self.mob.clear()
        self.Tel.clear()
        self.res.clear()


def checkemail(E):
    value = 0
    a = 0
    for i in E:
        if i == '@':
            value = 1
            a = E.index(i)
            print(a)

    if E[-4:] == '.com':
        value = 2

    return value


if __name__=="__main__":
    App=QApplication(sys.argv)
    win2 = window2()
    win1 = window1(win2)
    sys.exit(App.exec())