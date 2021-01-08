# sqlite database to manage employee database

import sqlite3
from datetime import datetime as date

connection = sqlite3.connect("employee_data.db", detect_types=sqlite3.PARSE_COLNAMES | sqlite3.PARSE_DECLTYPES)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE employee (
                                     id integer,
                                      first name text,
                                      last name text,
                                      email_id text,
                                      date_of_joining timestamp,
                                      salary integer,
                                      gender text)""")


class EmployeeDatabase:

    def __init__(self, select_employee=None):
        self.detail = select_employee

    @staticmethod
    def insert(value):

        with connection:
            cursor.execute("""INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?)""", value)

    @staticmethod
    def update(salary_, id_number):
        with connection:
            cursor.execute("""UPDATE employee set salary = ? where id = ?""", (salary_, id_number))

    @staticmethod
    def delete_employee(id_):
        with connection:
            cursor.execute("""DELETE from employee where id = ?""", (id_,))

    @classmethod
    def select_employee_by_first_name(cls, first_):
        cursor.execute("""SELECT * FROM employee WHERE first = ?""", (first_,))
        detail_ = cursor.fetchall()
        return cls(detail_)

    @classmethod
    def select_employee_by_last_name(cls, last_):
        cursor.execute("""SELECT * FROM employee WHERE last = ?""", (last_,))
        detail = cursor.fetchall()
        return cls(detail)

    @classmethod
    def select_employee_by_salary(cls, salary_):
        cursor.execute("""SELECT * FROM employee WHERE salary = ?""", (salary_,))
        detail = cursor.fetchall()
        return cls(detail)

    @classmethod
    def select_full_data(cls):
        cursor.execute("""SELECT * FROM employee""")
        detail = cursor.fetchall()
        return cls(detail)

    @classmethod
    def select_by_gender(cls, gender_):
        cursor.execute("""SELECT * FROM employee WHERE gender = ?""", (gender_,))
        detail = cursor.fetchall()
        return cls(detail)

    @classmethod
    def select_specific_person(cls, first_, last_):

        cursor.execute("""SELECT * FROM employee WHERE first = ? AND last = ?""", (first_, last_))
        detail = cursor.fetchall()
        return cls(detail)

    def sort(self):
        for row in self.detail:
            print(f"id :{row[0]}")
            print(f"first name :{row[1]}")
            print(f"last name : {row[2]}")
            print(f"email id : {row[3]} ")
            print(f"date of join : {row[4]}")
            print(f"salary : {row[5]}")
            print(f"gender : {row[6]}\n")


task = int(input("hi sir/madam which task are you looking for\n"
                 " 1.insert employee data\n2. update employee data\n"
                 "3. delete employee data\n4. select a employee data"))


if task == 1:
    no_of_member = int(input("enter the number of employee you want to enter"))
    for i in range(no_of_member):
        id_no = int(input("enter the employee id"))
        first_name = input("enter the employee's first name")
        last_name = input("enter the employee's last name")
        email_id = input("enter the employee's email id")
        date_of_joining = date.now()
        salary = int(input("enter the employee's salary"))
        gender = input("male or female")
        details = (id_no, first_name, last_name, email_id, date_of_joining, salary, gender)
        EmployeeDatabase().insert(details)

elif task == 2:
    person_id, salary = input("enter the id of the employee and enter the salary with space").split(" ")
    EmployeeDatabase().update(salary, person_id)

elif task == 3:
    person_id = input("enter the person id to delete the detail")
    EmployeeDatabase().delete_employee(person_id)

elif task == 4:
    sort = int(input("hello sir / madam which details are you looking for? \n"
                     " 1. filter the person by first name\n"
                     " 2. filter the person by last name\n"
                     " 3. filter the person by salary\n"
                     " 4. to view the full database\n"
                     " 5. filter the workers by gender\n"
                     " 6. filter for a specific person\n"))

    if sort == 1:
        option = input("enter the first name of the person")
        EmployeeDatabase.select_employee_by_first_name(option).sort()
    elif sort == 2:
        option = input("enter the last name of the person")
        EmployeeDatabase.select_employee_by_last_name(option).sort()
    elif sort == 3:
        option = int(input("enter the salary of the employee"))
        EmployeeDatabase.select_employee_by_salary(option).sort()

    elif sort == 4:
        EmployeeDatabase.select_full_data().sort()
    elif sort == 5:
        option = input("enter the gender to search")
        EmployeeDatabase.select_by_gender(option).sort()
    elif sort == 6:
        first, last = input("enter the first name and last name with space").split(" ")
        EmployeeDatabase.select_specific_person(first, last).sort()
