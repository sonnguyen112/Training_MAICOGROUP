import json
from datetime import datetime


class Employee():
    def __init__(self, full_name, date_of_birth, position, skills, start_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.position = position
        self.skills = skills
        self.start_year = start_year
    def save(self):
        file = open("employees.txt", "a")
        employee = {
            "full_name" : self.full_name,
            "date_of_birth" : self.date_of_birth,
            "position" : self.position,
            "skills" : self.skills,
            "start_year" : self.start_year
        }
        file.write(json.dumps(employee) + "\n")
        file.close()


class TechEmployee(Employee):
    def __init__(self, full_name, date_of_birth, position, skills, start_year, language_programming, projects):
        Employee.__init__(self, full_name, date_of_birth, position, skills, start_year)
        self.language_programming = language_programming
        self.projects = projects
    def save(self):
        Employee.save(self)
        file = open("tech_employees.txt", "a")
        tech_employee = {
            "full_name" : self.full_name,
            "date_of_birth" : self.date_of_birth,
            "position" : self.position,
            "skills" : self.skills,
            "start_year" : self.start_year,
            "language_programming" : self.language_programming,
            "projects" : self.projects
        }
        file.write(json.dumps(tech_employee) + "\n")
        file.close()


def create_employee(full_name, date_of_birth, position, skills, start_year):
    employee = Employee(full_name, date_of_birth, position, skills, start_year)
    employee.save()


def create_tech_employee(full_name, date_of_birth, position, skills, start_year, language_programming, projects):
    tech_employee = TechEmployee(full_name, date_of_birth, position, skills, start_year, language_programming, projects)
    tech_employee.save()


def create_list_participants_in_course():
    now = datetime.now()
    year_now = int(now.strftime("%Y"))
    employees = []
    file = open("employees.txt", "r")
    lines = file.readlines()
    for line in lines:
        employee = json.loads(line.replace("\n", ""))
        name_arr = employee["full_name"].split()
        employees.append((employee, len(employee["skills"]) * 10000 + (year_now - employee["start_year"])
         * 100 + (90 - ord(name_arr[len(name_arr) - 1][0].upper()))))
    file.close()
    results = sorted(employees, key = lambda x:x[1], reverse=True)
    print("LIST OF PARTICIPANTS IN COURSE:")
    for i in range(3):
        try:
            print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {results[i][0]["full_name"]}
    DOB : {results[i][0]["date_of_birth"]}
    Position : {results[i][0]["position"]}
    The number of skills : {len(results[i][0]["skills"])}
    Year start job: {results[i][0]["start_year"]}
            """)
        except:
            pass


def create_list_employee_use_python_and_more_project():
    num_of_employee = int(input("The number of employees: "))
    employees = []
    file = open("tech_employees.txt", "r")
    lines = file.readlines()
    for line in lines:
        employee = json.loads(line.replace("\n", ""))
        employees.append(employee)
    file.close()
    employees_use_python = list(filter(lambda x:"python" in x["language_programming"], employees))
    sort_employees_use_python_for_projects = sorted(employees_use_python, key=lambda x:len(x["projects"]), reverse=True)
    print("LIST OF EMPLOYEE USE PYTHON AND MORE PROJECT:")
    for i in range(num_of_employee):
        try:
            print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {sort_employees_use_python_for_projects[i]["full_name"]}
    DOB : {sort_employees_use_python_for_projects[i]["date_of_birth"]}
    Position : {sort_employees_use_python_for_projects[i]["position"]}
    Is use Python : {"python" in sort_employees_use_python_for_projects[i]["language_programming"]}
    The number of project : {len(sort_employees_use_python_for_projects[i]["projects"])}
            """)
        except:
            pass


def create_list_employee_under_30_and_projects_greater_5():
    now = datetime.now()
    year_now = int(now.strftime("%Y"))
    employees = []
    file = open("tech_employees.txt", "r")
    lines = file.readlines()
    for line in lines:
        employee = json.loads(line.replace("\n", ""))
        employees.append(employee)
    file.close()
    employees_under_30 = list(filter(lambda x:(year_now - int(x["date_of_birth"].split("/")[2])) >= 30, employees))
    employees_under_30_and_projects_greater_5 = list(filter(lambda x:len(x["projects"]) > 5, employees_under_30))
    print("LIST OF EMPLOYEES UNDER 30 AND HAVE GREATER 5 PROJECTS:")
    for i in range(len(employees_under_30_and_projects_greater_5)):
        print(f"""
+ EMPLOYEE {i + 1}:
    Full Name : {employees_under_30_and_projects_greater_5[i]["full_name"]}
    DOB : {employees_under_30_and_projects_greater_5[i]["date_of_birth"]}
    Position : {employees_under_30_and_projects_greater_5[i]["position"]}
    The number of projects : {len(employees_under_30_and_projects_greater_5[i]["projects"])}
        """)

# create_employee("Nguyen Van G", "02/02/2011", "junior", ["java", "c++", "JS", "Go"], 2008)
# create_tech_employee("Nguyen Van Khoa", "02/12/1975", "senior", ["english", "communicate", "dev"], 2009,
#  ["java", "c++"], ["project1", "project2", "project3", "project4", "project5", "project6"])
create_list_participants_in_course()
create_list_employee_use_python_and_more_project()
create_list_employee_under_30_and_projects_greater_5()