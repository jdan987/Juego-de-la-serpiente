import turtle
import time
import random

retraso = 0.1 #Velocidad de movimiento
marcador = 0
marcador_alto = 0


s = turtle.Screen()
s.setup(650,650) #'tup' de tupla
s.bgcolor('gray')
s.title("Proyecto Serpiente")

#Programamos a la serpiente
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
#Esto es el marcador:
texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\tMarcador más alto: 0", align='center', font=('verdana', 24, 'normal'))
#Movimiento de la serpiente:
def arriba():
    serpiente.direction = 'up'
def abajo():
    serpiente.direction = 'down'
def izquierda():
    serpiente.direction = 'left'
def derecha():
    serpiente.direction = 'right'

#Funciones del movimiento:

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

s.listen() #La pantalla escucha y ejecuta una función.
s.onkeypress(arriba, 'Up') #La pantalla recibe teclas
s.onkeypress(abajo, 'Down')
s.onkeypress(izquierda, 'Left')
s.onkeypress(derecha, 'Right')
while True:
    s.update() #actualiza la pantalla mostrando a la serpiente moviendose
    
    #Esto es para definir que cuando la serpiente toque un borde del plano cartesiano, pierda automáticamente
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
   
   
   
   
    if serpiente.distance(comida) < 20: #se pone '20' porque es el tamaño por defecto de la serpiente. así se marcau na hitbox más específica
        x = random.randint(-250,250) #Cuando la comdida es tocada por la serpiente esta se va a mover a un punto aleatorio en estas coordenadas
        y = random.randint(-250,250) #En ambos ejes ocurre
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
        
#Multiplicador del cuerpo
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
#Aquí estamos haciendo que la serpiente al tocarse a sí misma pierda 
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
                
            
    
    time.sleep(retraso) #'Sleep' es un elemento de 'time'









turtle.done()