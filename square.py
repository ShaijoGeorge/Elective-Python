from turtle import *
t=Turtle()
def square(t,l):
	for count in range(4):
		t.forward(l)
		t.left(90)
square(t,50)
