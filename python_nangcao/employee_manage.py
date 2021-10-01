import json
from datetime import datetime

EMPLOYEE_LIST = []
TECH_EMPLOYEE_LIST = []

class Employee():
    def __init__(self, full_name, date_of_birth, position, skills, start_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.position = position
        self.skills = skills
        self.start_year = start_year


class TechEmployee(Employee):
    def __init__(self, full_name, date_of_birth, position, skills, start_year, language_programming, projects):
        Employee.__init__(self, full_name, date_of_birth, position, skills, start_year)
        self.language_programming = language_programming
        self.projects = projects


def create_employee(full_name, date_of_birth, position, skills, start_year):
    employee = Employee(full_name, date_of_birth, position, skills, start_year)
    EMPLOYEE_LIST.append(employee)


def create_tech_employee(full_name, date_of_birth, position, skills, start_year, language_programming, projects):
    tech_employee = TechEmployee(full_name, date_of_birth, position, skills, start_year, language_programming, projects)
    EMPLOYEE_LIST.append(tech_employee)
    TECH_EMPLOYEE_LIST.append(tech_employee)


def create_list_participants_in_course():
    global EMPLOYEE_LIST
    now = datetime.now()
    year_now = int(now.strftime("%Y"))
    employees = []
    for employee in EMPLOYEE_LIST:
        name_arr = employee.full_name.split()
        employees.append((employee, len(employee.skills) * 10000 + (year_now - employee.start_year)
        * 100 + (90 - ord(name_arr[len(name_arr) - 1][0].upper()))))
    results = sorted(employees, key = lambda x:x[1], reverse=True)
    print("LIST OF PARTICIPANTS IN COURSE:")
    for i in range(3):
        try:
            print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {results[i][0].full_name}
    DOB : {results[i][0].date_of_birth}
    Position : {results[i][0].position}
    The number of skills : {len(results[i][0].skills)}
    Year start job: {results[i][0].start_year}
            """)
        except:
            return


def create_list_employee_use_python_and_more_project():
    global TECH_EMPLOYEE_LIST
    num_of_employee = int(input("The number of employees: "))
    employees_use_python = list(filter(lambda x:"python" in x.language_programming, TECH_EMPLOYEE_LIST))
    sort_employees_use_python_for_projects = sorted(employees_use_python, key=lambda x:len(x.projects), reverse=True)
    print("LIST OF EMPLOYEE USE PYTHON AND MORE PROJECT:")
    for i in range(num_of_employee):
        try:
            print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {sort_employees_use_python_for_projects[i].full_name}
    DOB : {sort_employees_use_python_for_projects[i].date_of_birth}
    Position : {sort_employees_use_python_for_projects[i].position}
    Is use Python : {"python" in sort_employees_use_python_for_projects[i].language_programming}
    The number of project : {len(sort_employees_use_python_for_projects[i].projects)}
            """)
        except:
            return


def create_list_employee_under_30_and_projects_greater_5():
    global TECH_EMPLOYEE_LIST
    now = datetime.now()
    year_now = int(now.strftime("%Y"))
    employees_under_30 = list(filter(lambda x:(year_now - int(x.date_of_birth.split("/")[2])) >= 30, TECH_EMPLOYEE_LIST))
    employees_under_30_and_projects_greater_5 = list(filter(lambda x:len(x.projects) > 5, employees_under_30))
    print("LIST OF EMPLOYEES UNDER 30 AND HAVE GREATER 5 PROJECTS:")
    for i in range(len(employees_under_30_and_projects_greater_5)):
        print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {employees_under_30_and_projects_greater_5[i].full_name}
    DOB : {employees_under_30_and_projects_greater_5[i].date_of_birth}
    Position : {employees_under_30_and_projects_greater_5[i].position}
    The number of projects : {len(employees_under_30_and_projects_greater_5[i].projects)}
        """)


create_employee("Nguyen Van A", "1/12/2002", "dev", ["dev"], 2010)
create_employee("Nguyen Van B", "8/1/2001", "dev", ["dev", "english"], 2011)
create_employee("Nguyen Van An", "8/1/2001", "dev", ["dev", "english", "communicate"], 2011)
create_employee("Nguyen Van Anh", "1/12/2002", "dev", ["dev"], 2009)
create_list_participants_in_course()

create_tech_employee("Nguyen Van C", "7/7/2020", "dev", ["dev", "english", "communicate"], 2008, ["c++"], ["project1"])
create_tech_employee("Nguyen Van D", "7/7/2020", "dev", ["dev", "english", "communicate"], 2008, ["python", "c++"], ["project1", "project2"])
create_tech_employee("Nguyen Van E", "7/7/1975", "dev", ["dev", "english", "communicate"], 1999, ["python", "c++"], ["project1", "project2",
"project3", "project4", "project5", "project6"])
create_list_employee_use_python_and_more_project()
create_list_employee_under_30_and_projects_greater_5()