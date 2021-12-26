import turtle
import random
wn=turtle.Screen()
turtle.bgcolor("black")
ig=turtle.Turtle()
ig.pensize(2)
res=5
rand_color=["white"]
for i in range(16):
	ig.color(random.choice(rand_color))
	res=res+5
	if i<=2:
		ig.right(90)
		ig.forward(2+res)
	elif i<=4:
		ig.right(90)
		ig.forward(4+res)
	elif i<=8 :
		ig.right(90)
		ig.forward(6+res)
	elif i<=10:
		ig.right(90)
		ig.forward(8+res)
	elif i<=12:
		ig.right(90)
		ig.forward(10+res)
	elif i<=14:
		ig.right(90)
		ig.forward(14+res)
	else :
		ig.right(90)
		ig.forward(16+res)
for i in range(16):
	ig.color("gray")
	res=res+5
	if i<=2:
		ig.right(90)
		ig.forward(18+res)
	elif i<=4:
		ig.right(90)
		ig.forward(20+res)
	elif i<=8 :
		ig.right(90)
		ig.forward(22+res)
	elif i<=10:
		ig.right(90)
		ig.forward(24+res)
	elif i<=12:
		ig.right(90)
		ig.forward(26+res)
	elif i<=14:
		ig.right(90)
		ig.forward(28+res)
	else :
		ig.right(90)
		ig.forward(30+res)
turtle.done()