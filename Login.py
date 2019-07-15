from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox,QDialog
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp, QMessageBox
from PyQt5.QtGui import QFont
import sys
import window3
from Database import database
from View import view_data
print('Login Window')


class Login(QDialog, database):

    """Constructor initializing line edit and setting its text placing line edits and label in Grid layout"""
    def __init__(self):
        database.__init__(self)
        QDialog.__init__(self)

        self.user = ''

        self.setStyleSheet(" colour: black ; font-size: 13pt ; font-family: arial")

        self.userNameLabel = QLabel("Username")
        self.userPassLabel = QLabel("Password")
        self.textName = QLineEdit(self)
        self.textName.setStyleSheet(" colour: black ; font-size: 11pt ; font-family: arial")
        self.textPass = QLineEdit(self)
        self.textPass.setStyleSheet(" colour: black ; font-size: 11pt ; font-family: arial")
        self.textPass.setEchoMode(QLineEdit.Password)

        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.setStyleSheet("background:teal; colour: white ; font-size: 13pt ; font-family: arial")
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QGridLayout(self)
        layout.addWidget(self.userNameLabel, 2, 1)
        layout.addWidget(self.userPassLabel, 3, 1)
        layout.addWidget(self.textName, 2, 2)
        layout.addWidget(self.textPass, 3, 2)
        layout.addWidget(self.buttonLogin, 4, 1, 1, 2)

        self.resize(370, 150)

        self.setWindowTitle("Login")

    def handleLogin(self):
        enrollment =''
        self.enroll_number = self.enrollment()
        if (self.textName.text() == 'admin'
                and self.textPass.text() == 'admin'):
            self.user = 'admin'
            QMessageBox.information(self, 'Successful', 'Logged in to Administrator')
            self.accept()
        elif self.textName.text() in self.enroll_number and self.textPass.text() == '':
            self.user = 'student'
            enrollment = "'"+self.textName.text()+"'"
            self.studentName = self.name(enrollment)
            QMessageBox.information(self, 'Successful', 'Logged in to '+str(self.studentName[0]))
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong User or Password')

    def __str__(self):
        return "'"+self.textName.text()+"'"

app = QApplication(sys.argv)
login = Login()
if login.exec_() == QDialog.Accepted:
    if login.user == 'admin':
        win3 = window3.window3()
    elif login.user == 'student':
        print("STUDENT")
        dataview = view_data(str(login))
sys.exit(app.exec_())