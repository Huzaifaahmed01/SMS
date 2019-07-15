from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QGridLayout, QDialog
import sys
import window4_5_6
from window1 import window1, window2

class window3(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui_win3()

    def init_ui_win3(self):

        self.entr_database = QPushButton('ENTER DATA BASE',self)
        self.edt_databsae = QPushButton('EDIT DATA BASE',self)
        self.updt_attend = QPushButton('UPDATE ATTENDENCE',self)
        self.updt_gpa = QPushButton('UPDATE GPA',self)

        self.entr_database.setStyleSheet("background:teal; color:yellow ; font-size: 13pt ; font-family: arial; font-weight: bold")
        self.edt_databsae.setStyleSheet("background:teal; color:yellow ; font-size: 13pt ; font-family: arial; font-weight: bold")
        self.updt_attend.setStyleSheet("background:teal; color:yellow; font-size: 13pt ; font-family: arial; font-weight: bold")
        self.updt_gpa.setStyleSheet("background:teal; color:yellow ; font-size: 13pt ; font-family: arial; font-weight: bold")

        layout_win3 = QGridLayout(self)
        layout_win3.addWidget(self.entr_database, 1, 1)
        layout_win3.addWidget(self.edt_databsae, 2, 1)
        layout_win3.addWidget(self.updt_attend, 3, 1)
        layout_win3.addWidget(self.updt_gpa, 4, 1)

        self.entr_database.clicked.connect(self.entr_db)
        self.edt_databsae.clicked.connect(self.edt_db)
        self.updt_attend.clicked.connect(self.updt_att)
        self.updt_gpa.clicked.connect(self.updtgpa)

        self.setWindowTitle("Admin")
        self.show()

    def entr_db(self):
        self.win2 = window2()
        self.win1 = window1(self.win2)

    def edt_db(self):
        self.win_4 = window4_5_6.window4()

    def updt_att(self):
        self.win_5 = window4_5_6.window5()

    def updtgpa(self):
        self.win_6 = window4_5_6.window6()

if __name__=="__main__":
    App=QApplication(sys.argv)
    window=window3()
    sys.exit(App.exec())
