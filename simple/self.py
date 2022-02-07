class Person():
	def __init__(self, name, age):
		self.age = age
		name = name # self.name
		print("I am a person")
	
	def hasLicense(self):
		if age >= 18: # self.age
			print("I can drive")
		else:
			print("I can't drive yet :(")
	
	def getName(self):
		return self.name

	def getAge(self):
		return self.age

if __name__ == "__main__":
    harry = Person("Harry", 18)
    harry.hasLicense()
    print(harry.getName())
    print(harry.getAge())