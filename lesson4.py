from turtle import Turtle
import turtle
class Ball(Turtle):
	def __init__(self, radius,color,dx,dy):
		Turtle.__init__(self)
		self.circle (radius)
		self.color (color)
		self.dx = dx
		self.dy = dy
	def d_x(self, num):
		dx=num*(self, dx+1)
	def dy(self, num):
		dy=num*(self, dy+1)

turtle.penup()
turtle.shape("circle")
turtle.penup()
ball1=Ball(10, "blue", 20, 30)









