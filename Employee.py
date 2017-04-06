

class Employee:
	'''This describes an employee in a company

		Methods:
		------------------
		set_title
		set_start_date
		set_name
		get_title
		get_start_date
		get_name
	'''

	def __init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def set_title(self, title):
		'''\This method sets the title of an employee

		Method Arguments:
		------------------
		title(string): An employee position'''

		self.title = title

	def set_start_date(self, start_date):
		'''\This method sets the start_date of an employee

		Method Arguments:
		------------------
		start_date(string): This is a date in the format mm/dd/yyyy on which
		the employee has begun or will begin work at the company'''

		self.start_date = start_date

	def set_name(self, name):
		'''\This method sets the name of an employee

		Method Arguments:
		------------------
		name(string): This is an employee's name'''

		self.name = name

	def get_title(self):
		'''\This method returns the title of an employee'''

		return self.title

	def get_start_date(self):
		'''\This method returns the start_date of an employee.'''

		return self.start_date

	def get_name(self):
		'''\This method returns the name of an employee'''

		return self.name

