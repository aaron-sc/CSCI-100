import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

turtle.colormode(255)


tess = turtle.Turtle()
tess.pensize(10)
tess.speed(1000)

for x in range(0,255):
	if(x % 2 == 0):
		tess.pencolor(x,0,0)
	elif(x % 3 == 0):
		tess.pencolor(0,x,0)
	else:
		tess.pencolor(0,0,x)
	tess.forward(x+10)
	tess.left(120)
	tess.forward(60)

tess.penup()
tess.goto(-15,-200)
tess.pendown()
style = ("Courier", 30)
tess.write("Oblivion", font=style, align="center")

wn.exitonclick()