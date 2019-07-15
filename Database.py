import sqlite3
from PyQt5.QtWidgets import QMessageBox
from abc import ABC, abstractmethod


class database:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS personal_info(
        enrollment_number TEXT,
        student_name TEXT,
        student_cnic TEXT,
        fathers_name TEXT,
        fathers_cnic TEXT,
        date_of_birth TEXT,
        gender INTEGER,
        permanent_address TEXT,
        religion INTEGER,
        nationality TEXT,
        country TEXT,
        city TEXT,
        email TEXT,
        mobile REAL,
        telephone REAL,
        Residence TEXT
        )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS academic_info(
                enrollment_number TEXT,
                roll_number INTEGER,
                section INTEGER,
                department TEXT,
                batch TEXT,
                shift INTEGER,
                year INTEGER,
                attendance REAL,
                cgpa REAL
                )""")

    def view_academic_info(self, enroll):
        self.c.execute("SELECT * FROM academic_info WHERE enrollment_number ="+ enroll)
        data = self.c.fetchone()

        if not data:
            QMessageBox.warning(self, 'Error', 'Could not find any academic info with enroll no', enroll)
            return None

        self.academic_list = []
        for i in range(9):
            self.academic_list.append(data[i])
        self.c.close()
        self.conn.close()

    def view_personal_info(self, enroll):
        self.c.execute("SELECT * FROM personal_info WHERE enrollment_number ="+enroll)
        data = self.c.fetchone()

        if not data:
            QMessageBox.warning(self, 'Error', 'Could not find any personal info with enroll no', enroll)
            return None

        self.personal_list = []
        for i in range(16):
            self.personal_list.append(data[i])
        self.c.close()
        self.conn.close()

    def enter_database(self, per, acad):
        try:
            self.c.execute("INSERT into personal_info(enrollment_number,student_name,student_cnic,fathers_name,"
                           "fathers_cnic,date_of_birth,gender,permanent_address,religion,nationality,country,city,"
                           "email,mobile,telephone,Residence) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                           , (acad[0],per[0],per[1],per[2],per[3],per[4],int(per[5]),per[6],int(per[7]),per[8],per[9]
                              ,per[10],per[11],float(per[12]),float(per[13]),per[14]))
            self.c.execute("INSERT into academic_info(enrollment_number,roll_number,section,department,batch,shift,"
                           "year,attendance,cgpa) VALUES(?,?,?,?,?,?,?,?,?)"
                           ,(acad[0],int(acad[1]),int(acad[2]),acad[3],acad[4],int(acad[5]),int(acad[6]),float(acad[7]),float(acad[8])))
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(self,'Error','Could not add Student to database.')

    def update_attendance(self, enroll, attendance):
        try:
            self.c.execute("UPDATE academic_info SET attendance = ? WHERE enrollment_number = ?", (attendance, enroll))
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(self, 'Error', 'Could not update attendance of enroll no.'+enroll)

    def update_gpa(self, gpa, enroll):
        try:
            self.c.execute("UPDATE academic_info SET cgpa = ? WHERE enrollment_number = ?", (gpa, enroll))
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(self, 'Error', 'Could not update attendance of enroll no.'+enroll)

    def enrollment(self):
        self.enr_list = []
        try:
            self.c.execute("SELECT enrollment_number FROM personal_info")
            data = self.c.fetchall()
            for i in range(len(data)):
                self.enr_list.append(data[i][0])
            return self.enr_list
        except Exception:
            QMessageBox.warning(self,'Error','Not able to fetch enrollment Numbers.')

    def name(self, enroll):
        #enroll = "'"+enroll+"'"
       # try:
            self.c.execute("SELECT student_name FROM personal_info WHERE enrollment_number = "+str(enroll))
            data = self.c.fetchone()
            self.c.close()
            self.conn.close()
            return data

if __name__ == '__main__':
    db = database()