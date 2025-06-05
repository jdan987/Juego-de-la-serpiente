import turtle
import time
import random

retraso = 0.1 # speed snake
marcador = 0
marcador_alto = 0


s = turtle.Screen()
s.setup(650,650) #'tup' de tupla
s.bgcolor('gray')
s.title("Proyecto Serpiente")

#We make the Snake´s code
serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('red')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)

cuerpo = []
#This is the scoreboard
texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\tMarcador más alto: 0", align='center', font=('verdana', 24, 'normal'))
#Snake movements
def arriba():
    serpiente.direction = 'up'
def abajo():
    serpiente.direction = 'down'
def izquierda():
    serpiente.direction = 'left'
def derecha():
    serpiente.direction = 'right'

#We program the movements

def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)

s.listen() #The screen listens and executes the function
s.onkeypress(arriba, 'Up') #programmed keys
s.onkeypress(abajo, 'Down')
s.onkeypress(izquierda, 'Left')
s.onkeypress(derecha, 'Right')
while True:
    s.update() #Update the screen and show the movement 
    
    #This is to define that when the snake touches an edge of the Cartesian plane, it automatically loses
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'
        serpiente.clear()
    
        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcador_alto), align='center', font=("verdana", 24, 'normal'))
   
   
   
   
    if serpiente.distance(comida) < 20: #'20' is set because it's the snake's default size. This way, a more specific hitbox is marked.
        x = random.randint(-250,250) #When the food is touched by the snake it will move to a random point at these coordinates
        y = random.randint(-250,250) #It occurs on both axes
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('red')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcador_alto), align='center', font=("verdana", 24, 'normal'))
        
#Body multiplier
    total = len(cuerpo)
    for i in range(len(cuerpo)-1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()
#Here we are making the snake lose its touch 
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
                
            
    
    time.sleep(retraso) #'Sleep' es un elemento de 'time'
turtle.done()
