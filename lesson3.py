class Animal(object):
	def __init__(self, name, age, color, favorite_color):
		self.name = name
		self.age = age
		self.color = color
		self.favorite_color = favorite_color

	def eat(self,food):
		print(self.name + ' is eating ' + food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favorite_color)
	def make_sound(self):
		print('the ' + self.name + sound)
animal1 = Animal('dog', 12, 'brown', 'blue')
animal1.eat('pizza')
animal1.description()
animal1.make_sound()








