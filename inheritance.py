class Student(object):
	"""class for student"""

	def __init__(self, name,regNo,unit):
		self.name=name
		self.reg_no=regNo
		self.unit=unit

	def get_name(self):
		return self.name

	def get_regNo(self):
		return self.regNo

	def get_unit(self):
		return self.unit

class Cat(Student):
	"""class for Cat which inherits from student"""

	super.__init__

	def cat_marks(self, cmarks):
		self.cmarks=cmarks

	def get_marks(self):
		return self.cmarks

class Assignment(Student):
	"""class for Assignment"""

	def assyn(self,amarks):
		self.amarks=amarks

	def get_amarks(self):
		return self.amarks

class Exam(Assignment):
	"""class for Exam"""
	def __init__(self, emark):
		self.emark=emark

		super.__init__

	def total(a,b,total):
		cat = Cat
		assign= Assignment
		a=cat.get_marks
		b=assign.get_amarks

		total=a+b+self.emark
		return total
		
		
if __name__ == '__main__':

	b=Cat("dianah",2017,"Business process modelling")

	c=Assignment("dianah",2017,"Business process modelling")

	d=Exam(55)

	a=Student("dianah",2017,"Business process modelling")
	

		
