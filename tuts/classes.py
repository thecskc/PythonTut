class Animal:
	def __init__(self):
		print("Animal Created")

	def animal(self):
		print("I am an animal")



class Duck(Animal): #Duck inherits from Animal
	def __init__(self,duckName,**kwargs):
		self.name = duckName
		super(Duck, self).__init__() #constructor needs to be explicitly
									# if required.
		self.kwargDict = kwargs

	def printKwargs(self):
		for key in self.kwargDict:
			print(key,self.kwargDict.get(key))



	def quack(self):
		print("Quack!")
		self.animal()
	def walk(self):
		print("Duck Walking!")



def main():
	donald = Duck("Donald The Duck",color="Red")

	print("Created {}".format(donald.name))
	donald.quack()
	donald.walk()
	donald.printKwargs()

	# dictionary = dict(color = "Red",num = 100)
	# print(dictionary["color"])
	# dictionary = {"color":"blue"}
	# print(dictionary["color"])

#NOTE: There are NO access modifiers in Python. So there's no 
# explicit way of creating private members or anything like that.
#Also, python child classes don't call the constructor or the destructor
# of the parent classes automatically.
# What this means is that accessor methods aren't really required.
# But it's still a good idea to have get and set methods to access member variables
# because you can make additional modifications to the properties of the object if required.


main();
