from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox,QDialog
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp, QMessageBox
from PyQt5.QtGui import QFont
import sys
import window3
from Database import database


class EditPersonal(database, QDialog):
    def __init__(self, enroll):
        QDialog.__init__(self)
        database.__init__(self)

        self.enroll = enroll

        self.view_personal_info(enroll)

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
        self.res = QLineEdit(self)

        self.g = QComboBox(self)
        self.Re=QComboBox(self)

        self.init_ui_pers()

        self.set_text()

    def set_text(self):
        self.Fname.setText(self.personal_list[1])
        self.c1.setText(self.personal_list[2])
        self.Ftname.setText(self.personal_list[3])
        self.c2.setText(self.personal_list[4])
        self.dob.setText(self.personal_list[5])
        self.Add.setText(self.personal_list[7])
        self.Na.setText(self.personal_list[9])
        self.count.setText(self.personal_list[10])
        self.city.setText(self.personal_list[11])
        self.Email.setText(self.personal_list[12])
        self.mob.setText(str(self.personal_list[13]))
        self.Tel.setText(str(self.personal_list[14]))
        self.res.setText(self.personal_list[15])
        self.g.setCurrentIndex(self.personal_list[6])
        self.Re.setCurrentIndex(self.personal_list[8])

    def init_ui_pers(self):

        self.setStyleSheet("font-size: 13pt ; font-family: arial")

        self.resize(700, 500)

        # PushButtons Defined
        self.edit = QPushButton(self)
        self.reset = QPushButton(self)

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
        self.edit.setText('Edit')
        self.reset.setText('Reset')

        # ComboBox i.e Drop down menus
        self.g.addItem("Male")
        self.g.addItem("Female")
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

        self.Grid.addWidget(self.edit, 16, 2)
        self.Grid.addWidget(self.reset, 16, 1)

        # function map to button click
        self.edit.clicked.connect(self.edit_func)
        self.reset.clicked.connect(self.reset_func)

        # title
        self.setWindowTitle('STUDENT MODULE')

        self.show()

    def edit_func(self):
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
            string = self.Fname.text() + "|" + self.c1.text() + "|" + self.Ftname.text() + "|" + self.c2.text() + "|" +\
                     self.dob.text() + "|" + str(self.g.currentIndex()) + "|" + self.Add.text() + "|" + str(self.Re.currentIndex())\
                     + "|" + self.Na.text()+ "|" + self.count.text() + "|" + self.city.text() + "|" + self.Email.text()\
                     + "|" + self.mob.text() + "|" + self.Tel.text() + "|" + self.res.text()
            st = string.split('|')
            self.enter_database(st)
            QMessageBox.information(self, 'Successful', 'Personal Info has been updated for enroll ' + self.enr.text())
            self.accept()

    def enter_database(self, lst):
        try:
            self.c.execute("UPDATE personal_info SET student_name = ? ,student_cnic = ? ,fathers_name = ? ,"
                           "fathers_cnic = ? ,date_of_birth = ? ,gender = ? ,permanent_address = ? ,religion = ? ,"
                           "nationality = ? ,country = ? ,city = ? ,email = ? ,mobile = ? ,telephone = ? ,"
                           "Residence = ? WHERE enrollment_number = ?"
                           ,(lst[0],lst[1],lst[2],lst[3],lst[4],int(lst[5]),lst[6],int(lst[7]),lst[8],lst[9]
                             ,lst[10],lst[11],float(lst[12]),float(lst[13]),lst[14]), self.enroll)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(self, 'Error', 'Could not Update Student with enroll:'+self.enroll)

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


class EditAcademic(database, QDialog):
    def __init__(self, enroll):
        QDialog.__init__(self)
        database.__init__(self)

        self.view_academic_info(enroll)

        ##textBoxes defined
        self.enroll = QLineEdit(self)
        self.roll = QLineEdit(self)
        self.dept = QLineEdit(self)
        self.batch = QLineEdit(self)
        self.attend = QLineEdit(self)
        self.cgpa = QLineEdit(self)

        self.sec = QComboBox(self)
        self.shift = QComboBox(self)
        self.year = QComboBox(self)

        self.init_ui_acad()

        self.set_text()

    def set_text(self):
        self.enroll.setText(self.academic_list[0])
        self.roll.setText(str(self.academic_list[1]))
        self.dept.setText(self.academic_list[3])
        self.batch.setText(str(self.academic_list[4]))
        self.attend.setText(str(self.academic_list[7]))
        self.cgpa.setText(str(self.academic_list[8]))
        self.sec.setCurrentIndex(self.academic_list[2])
        self.shift.setCurrentIndex(self.academic_list[5])
        self.year.setCurrentIndex(self.academic_list[6])

    def init_ui_acad(self):
        self.setStyleSheet("font-size: 13pt ; font-family: arial")
        self.resize(400, 200)

        ##pushbutton defined
        self.edit = QPushButton(self)
        self.reset_win2 = QPushButton(self)

        ##setting text to buttons
        self.edit.setText('Edit')
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

        self.sec.addItem("A")
        self.sec.addItem("B")
        self.sec.addItem("C")
        self.sec.addItem("D")

        self.shift.addItem("Morning")
        self.shift.addItem("Evening")

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

        self.Grid_win.addWidget(self.edit, 10, 1)
        self.Grid_win.addWidget(self.reset_win2, 10, 2)

        # connect to function
        self.edit.clicked.connect(self.edit_func)
        self.reset_win2.clicked.connect(self.reset_win2_func)

        self.setWindowTitle('student management system')

        self.show()

    def edit_func(self):
        if self.enroll.text()=='' or self.roll.text()=='' or self.dept.text()=='' or self.batch.text()=='' or self.attend.text()=='' or self.cgpa.text() == '':
            QMessageBox.warning(self, 'Error', 'Fields is/are left to fill')
        elif enrollment(self.enroll.text()) == False:
            QMessageBox.warning(self, 'Error', 'Enrollment entered is wrong')
        elif float(self.cgpa.text())>4.0:
            QMessageBox.warning(self, 'Error', 'CGPA must not exceed 4.0')
        elif float(self.attend.text())>100:
            QMessageBox.warning(self, 'Error', 'Attendance must not exceed 100')
        else:
            acad = self.enroll.text() + '|' + self.roll.text() + '|' + str(self.sec.currentIndex()) + '|' + self.dept.text()\
                   + '|' + self.batch.text() + '|' + str(self.shift.currentIndex()) + '|' + str(self.year.currentIndex())\
                   + '|' + self.attend.text() + '|' + self.cgpa.text()
            self.academiclist = acad.split('|')
            self.enter_database(self.academiclist)
            QMessageBox.information(self, 'Successful', 'Academic Info has been updated for enroll ' + self.enr.text())
            self.accept()

    def enter_database(self, lst):
        try:
            self.c.execute("UPDATE academic_info SET roll_number = ? , section = ? , department = ? , batch = ? ,"
                           " shift = ? , year = ? , attendance = ? , cgpa = ? WHERE enrollment_number = ?"
                           , (int(lst[1]), int(lst[2]), lst[3], lst[4], int(lst[5]), int(lst[6]), float(lst[7]), float(lst[8]),
                              lst[0]))
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(self, 'Error', 'Could not Update Student with enroll:' + self.enroll)

    def reset_win2_func(self):
        self.enroll.clear()
        self.roll.clear()
        self.dept.clear()
        self.batch.clear()
        self.attend.clear()
        self.cgpa.clear()


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


def enrollment(enr):
    if enr[:2].isalpha() and enr[3:].isdigit():
        return True
    else:
        return False


enr = "'cs-12349'"
if __name__=="__main__":
    App=QApplication(sys.argv)
    window=EditPersonal(enr)
    sys.exit(App.exec())
