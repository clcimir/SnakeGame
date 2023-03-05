import turtle as t
import time
import random

delay=0.1

wn=t.Screen()
wn.title('Test game')
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.tracer(0)


head = t.Turtle()
head.shape('square')
head.color('white')
head.penup()

food = t.Turtle()
food.shape('square')
food.color('red')
food.penup()
food.setpos(random.randrange(-280, 280, 20),
random.randrange(-280, 280, 20))

body = list()
for i in range(3):
    tmp = t.Turtle()
    tmp.shape('square')
    tmp.color('light green')
    tmp.penup()
    tmp.setpos(-20-20*i, 0)
    if i>0:
        tmp.color('light green')
    body.append(tmp)

def goleft():
    if head.heading()!=0:
        head.setheading(180)

def goright():
    if head.heading()!=180:
        head.setheading(0)
    
def goup():
    if head.heading()!=270:
        head.setheading(90)
    
def godown():
    if head.heading()!=90:
        head.setheading(270)
    
wn.listen()
wn.onkeypress(goleft,  "a")
wn.onkeypress(goright, "d")
wn.onkeypress(goup,    "w")
wn.onkeypress(godown,  "s")

i=0

sc=t.Screen()
sc.title('Test game')
#wn.bgpic("C:\\Users\\serit\\Documents\\programm\\snake\\background.gif")
sc.bgcolor('black')
sc = t.Turtle()
sc.penup()
sc.color('white')
sc.setpos(350,260)
sc.hideturtle()
sc.write('Score: {}'.format(i), font=("Arial", 24, "bold"))

while True:
    wn.update()

    if head.distance(food) < 10:
        food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
        i+=1
        sc.clear()
        sc.setpos(350,260)
        sc.write('Score: {}'.format(i), font=("Arial", 24, "bold"))
        tmp = t.Turtle()
        tmp.shape('square')
        tmp.color('light green')
        tmp.penup()
        body.append(tmp)

    xy = head.pos()
    for bp in body:
        xyloc = bp.pos()
        bp.setpos(xy)
        xy = xyloc
    head.forward(20)
    time.sleep(delay)
    
    if head.xcor()>300:
        head.setx(-300)
        
    if head.ycor()>300:
        head.sety(-300)
        
    if head.xcor()<-300:
        head.setx(300)
        
    if head.ycor()<-300:
        head.sety(300)
