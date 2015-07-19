import turtle


def draw_square(new_turtle):
	for i in range(0,4):
		new_turtle.forward(150)
		new_turtle.right(90)


def draw_art():
	window = turtle.Screen()#create a new frame
	window.bgcolor("black")#set the background color to green
	
	
	flower = turtle.Turtle()#init a new turtle
	flower.shape("arrow")#set the share to circle
	flower.color("white")#set the color to white
	flower.speed(20)#speed to 2
	x= 1
	for i in range(1,37):
		flower.circle(60)
		flower.right(20)
	
	while x < 37:
		draw_square(flower)#call the function and put parameter 
		flower.right(10)
		x += 1 
	flower.pensize(10)
	flower.right(90)
	flower.forward(350)

	window.exitonclick()#Make sure to position this last

draw_art()#implementation			
