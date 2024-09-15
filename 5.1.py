class StringVar:
	
	def __init__(self,string = 'Some info'):
	    self._string = string 

	def get_string(self):
		return self._string

	def set_string(self,a):
		self._string = a

s = StringVar()
print(s._string)
# Добавляем в строку
s.set_string('New info')

# Получение информации
print(s.get_string())

print(s._string)