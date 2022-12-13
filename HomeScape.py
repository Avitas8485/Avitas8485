#  File: HomeScape.py
#  Name: Avity Ngonyani  
#  Email: avity4585@gmail.com
#  Date: 11/7/2022
#  Description of Program: using turtle to draw a house


import turtle
count = 0
turtle.speed(0)
#sky
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(1000)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.end_fill()
# front wall
turtle.fillcolor('light pink')
turtle.begin_fill()
turtle.backward(200)
turtle.right(90)
turtle.backward(100)
turtle.right(90)
turtle.backward(200)
turtle.right(90)
turtle.backward(100)

# side wall
turtle.right(45)
turtle.forward(70)
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.forward(70)
turtle.end_fill()

# ceiling
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.right(45)
turtle.forward(200)
turtle.right(100)
turtle.forward(100)
turtle.right(80)
turtle.forward(200)
turtle.right(100)
turtle.forward(100)
turtle.end_fill()

# top side wall
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.left(145)
turtle.forward(70)
turtle.left(79)
turtle.forward(59)
turtle.left(136.5)
turtle.forward(102)
turtle.end_fill()

# side window 1
turtle.up()
turtle.left(9.5)
turtle.forward(25)
turtle.left(135)
turtle.forward(10)
turtle.down()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(20)
turtle.right(135)
turtle.forward(30)
turtle.right(45)
turtle.forward(20)
turtle.right(135)
turtle.forward(30)
turtle.end_fill()
turtle.up()
turtle.right(45)
turtle.forward(10)
turtle.right(135)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.right(135)
turtle.forward(10)
turtle.right(45)
turtle.forward(10)
turtle.right(45)
turtle.down()
turtle.forward(20)

# side window 2
turtle.up()
turtle.left(45)
turtle.forward(5)
turtle.right(45)
turtle.forward(10)
turtle.down()

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(20)
turtle.right(135)
turtle.forward(30)
turtle.right(45)
turtle.forward(20)
turtle.right(135)
turtle.forward(30)
turtle.end_fill()

turtle.up()
turtle.right(45)
turtle.forward(10)
turtle.right(135)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.right(135)
turtle.forward(10)
turtle.right(45)
turtle.forward(10)
turtle.right(45)
turtle.down()
turtle.forward(20)

turtle.up()
turtle.left(45)
turtle.forward(5)
turtle.right(45)

turtle.forward(10)
turtle.down()

turtle.right(135)
turtle.forward(70)
turtle.right(45)
turtle.forward(70)
turtle.right(45)
turtle.forward(25)
turtle.right(90)
turtle.up()
turtle.forward(85)
turtle.down()
# front windows
def window():
    count = 0
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    while count < 4:
        turtle.left(90)
        turtle.forward(40)
        count = count + 1
    turtle.end_fill()
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
window()
def space_btn_window():
    turtle.up()
    turtle.right(90)
    turtle.forward(20)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.down()
space_btn_window()
window()
# door
turtle.up()
turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.down()
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.forward(45)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(30)
turtle.end_fill()

turtle.up()
turtle.forward(80)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.down()

# ground
turtle.fillcolor('green')
turtle.begin_fill()
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(1000)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(18)
turtle.right(45)
turtle.forward(70)
turtle.right(45)
turtle.forward(200)
turtle.right(90)
turtle.forward(67)
turtle.end_fill()

turtle.left(90)
turtle.forward(50)
# tree
def the_trees():
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.right(180)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(2)
    turtle.left(90)
    def circle_me1():
        
        turtle.fillcolor('green')
        turtle.begin_fill()
        count = 0 
        while(count < 360):
            turtle.forward(0.3) 
            turtle.left(1) 
            count = count + 1
        count = 0
        while(count < 180):
            turtle.forward(0.3) 
            turtle.left(1) 
            count = count + 1
        turtle.end_fill()
    def circle_me2():
        turtle.right(180)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.fillcolor('green')
        turtle.begin_fill()
        
        count = 0
        while(count < 360): 
            turtle.forward(0.25) 
            turtle.left(1) 
            count = count + 1
        count = 0
        while(count < 180):
            turtle.forward(0.25) 
            turtle.left(1) 
            count = count + 1
        turtle.end_fill()
    def circle_me3():
        turtle.right(180)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.fillcolor('green')
        turtle.begin_fill()
        
        count = 0
        while(count < 360): 
            turtle.forward(0.2) 
            turtle.left(1) 
            count = count + 1
        count = 0
        while(count < 180):
            turtle.forward(0.2) 
            turtle.left(1) 
            count = count + 1
        turtle.end_fill()
    circle_me1()
    circle_me2()
    circle_me3()
    
the_trees()
turtle.up()
turtle.left(90)
turtle.forward(85)

turtle.right(90)
turtle.forward(90)
turtle.down()
the_trees()
turtle.up()
turtle.left(90)
turtle.forward(85)

turtle.right(90)
turtle.forward(90)
turtle.down()
the_trees()
turtle.up()
turtle.left(90)
turtle.forward(85)

turtle.left(90)
turtle.forward(800)

turtle.right(180)

turtle.down()
the_trees()
turtle.up()
turtle.left(90)
turtle.forward(85)

turtle.right(90)
turtle.forward(90)
turtle.down()
the_trees()

turtle.up()
turtle.left(90)
turtle.forward(85)
turtle.right(90)
turtle.forward(90)
turtle.down()

the_trees()

turtle.up()
turtle.left(90)
turtle.forward(300)
turtle.down()
def cloud():
    radius = 20
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.right(90)
    turtle.circle(radius, 180)
    turtle.right(180)
    turtle.circle(radius, 180)
    turtle.right(90)
    turtle.circle(radius, 180)
    turtle.right(90)
    turtle.circle(radius, 90)
    turtle.right(45)
    turtle.circle(radius, 90)
    turtle.right(90)
    turtle.circle(radius, 155)
    turtle.end_fill()




cloud()
turtle.up()
turtle.goto(0, 300)
turtle.down()
cloud()
turtle.up()
turtle.goto(-200, 300)
turtle.down()
cloud()
turtle.up()
turtle.goto(300, 300)
turtle.down()
cloud()
def flower():
    import random
    turtle.pensize(1.3)
    colors = ['red', 'yellow', 'blue', 'pink', 'purple']
    color = random.choice(colors)
    turtle.fillcolor(color)
    turtle.begin_fill() 

    for i in range(4):
        turtle.circle(16, 50)
        turtle.circle(4, 180)
        turtle.left(180)
        turtle.circle(4, 180)
        turtle.circle(16, 50)
        turtle.left(180)
    turtle.end_fill() 

    turtle.right(90)
    turtle.circle(-40, 80)

turtle.mainloop()