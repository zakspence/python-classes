from Company import *
from Employee import *

a_company = Company('Heartbreak Hotel', 'Hotels and Hospitality')

an_employee = Employee('Zak Spence', 'Software Developer', '12/31/2019')
another_employee = Employee('Donald Glover', 'Rapper', '12/12/2012')
yet_another_employee = Employee('Ramona Quinby', 'Software Developer', '09/15/1998')

a_company.add_employee(an_employee)
a_company.add_employee(another_employee)
a_company.add_employee(yet_another_employee)

company_employees = a_company.get_employees()

for employee in company_employees:
    print(employee.get_name())