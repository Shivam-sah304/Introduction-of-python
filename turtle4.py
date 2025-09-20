import turtle
tp=turtle.Screen()
tp.title("Writing inside the box")
tp.bgcolor("white")
tr=turtle.Turtle()
tr.hideturtle()
tr.up()
tr.goto(-300,150)
tr.down()
tr.fillcolor("khaki")
tr.begin_fill()
tr.forward(600)
tr.left(90)
tr.forward(100)
tr.left(90)
tr.forward(600)
tr.left(90)
tr.forward(100)
tr.goto(-300,175)
tr.end_fill()
tr.write("Hello Shivam Sir!!!!!",font=("Arial",40,"bold"))
tr.up()
tr.goto(0,0)

tr.down()
tr.right(90)
tr.forward(300)
tr.left(90)
tr.forward(100)
tr.left(90)
tr.forward(300)
tr.left(90)
tr.forward(100)
x=-230
y=-75
tr.right(90)
for i in range(6):
    tr.up()
    tr.goto(x,y)
    x=x+30
    
    tr.down()
    
    a=input("enter one string")
    tr.write(a,font=("Arial",15,"bold"))
    tr.forward(20)

turtle.done()