import turtle
import random


w = turtle.Screen()
w.title("Primer proyecto")
w.bgcolor("gray")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#Características de las tortugas:
jugador1.hideturtle() #Oculta la tortuga
jugador1.shape("turtle")
jugador1.color("red", "red")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

#Ordenes para tortugas:
jugador1.penup()
jugador1.goto(200, 100)
jugador1.pendown()
jugador1.circle(30)
jugador1.penup()
jugador1.goto(-200, 125)
jugador1.pendown()
jugador1.showturtle() #hace aparecer la tortuga

jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.circle(30)
jugador2.penup()
jugador2.goto(-200, -180)
jugador2.pendown()
jugador2.showturtle()

dado = [1, 2, 3, 4, 5, 6] #USamos una lista para establecer el dado. también se pueden usar tupplas

#Establecemos el parámetro para ganar el juego usando bucles y condicionales
for i in range(20):
    if jugador1.pos() >= (150, 200): #Con "pos()" condicionamos que al llegar a un número de pasos el juego termina, este método devuelve las coordenadas en que está la tortuga
        print("Tortuga Roja Gana!")
        break
    elif jugador2.pos() >= (150,200):
        print("Tortuga Azul Gana!!")
        break
    else:
        input("presiona la tecla Enter para avanzar")
        turno1 = random.choice(dado)
        print("Tu número es:",turno1, "\nAvanzas:",turno1 * 20)
        jugador1.forward(20*turno1)

        input("presiona la tecla Enter para avanzar")
        turno2 = random.choice(dado)
        print("Tu número es:",turno2, "\nAvanzas:",turno2 * 20)
        jugador2.forward(20*turno2)

turtle.done()
