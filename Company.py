

class Company:
    """This represents a company in which people work

    Methods:
        ------------------
        set_name
        set_industry
        get_name
        get_industry
        add_employee
    """

    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.employees = list()

    def set_name(self, name):
        '''\This method sets the name of the company

        Method Arguments:
        ------------------
        name(string): This is the company's name'''

        self.name = name

    def get_name(self):
        """Returns the name of the company"""

        return self.name

    def set_industry(self, industry):
        '''\This method sets the industry of the company

        Method Arguments:
        ------------------
        industry(string): This is the company's industry'''

        self.industry = industry

    def get_industry(self):
        """Returns the industry of the company"""

        return self.industry

    def add_employee(self, employee):
        '''\This method adds an employee to the company

        Method Arguments:
        ------------------
        employee(object): This is an employee of the company'''

        self.employees.append(employee)

    def get_employees(self):
        """Returns the employees of the company"""

        return self.employees

