from Company import *
from Employee import *

a_company = Company('Heartbreak Hotel', 'Hotels and Hospitality')

an_employee = Employee('Zak Spence', 'Software Developer', '12/31/2019')
a_company.add_employee(an_employee)

company_employees = a_company.get_employees()

for employee in company_employees:
    print(employee.name)