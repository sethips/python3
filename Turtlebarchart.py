import turtle

def drawBar(t,height):
	t.begin_fill()
	t.left(90)
	t.forward(height)
	t.write(str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.end_fill()

xs=[48,117,200,240,160,260,220]
maxheight = max(xs)
numbars=len(xs)
border=10

tess = turtle.Turtle()
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border,maxheight+border)

for a in xs:
	drawBar(tess, a)

wn.exitonclick()