 # CLASSES & OBJECTS

class Person:
	__name = ''
	__email = ''

	def __init__(self, name, email):
		self.__name = name
		self.__email = email

	def set_name(self, name):
		self.__name = name
	def get_name(self):
		return self.__name

	def set_email(self, email):
		self.__email = email
	
	def get_email(self):
		return self.__email
	def toString(self):
		return '{} can be contacted at {}'.format(self.__name, self.__email)

Godfrey = Person('Godfrey Atima', 'godfreyatima@gmail,com')
#Godfrey.set_name('Godfrey Atima')
#Godfrey.set_email('godfreyatima@gmail.com')

print(Godfrey.toString())
