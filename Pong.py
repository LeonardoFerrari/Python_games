import turtle

jogo = turtle.Screen()
jogo.title("Teste")
jogo.bgcolor('pink')
jogo.setup(width=800, height=600)
jogo.tracer()

# Barra
barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("classic")
barra_a.color("black")
barra_a.penup()
barra_a.goto(-350,0)

barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("classic")
barra_b.color("black")
barra_b.penup()
barra_b.goto(350,0)
#Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color("black")
bola.penup()
bola.dx = 2
bola.dy = -2

# Funções

def mover_cima_a():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)
    barra_a.shapesize(1.0, 1.0, 1)
    barra_a.tilt(-3000)

def mover_baixo_a():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)
    barra_a.resizemode('user')
    barra_a.shapesize(5, 5, 12)
    barra_a.tilt(3000)

def mover_cima_b():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)
    barra_b.shapesize(1.0, 1.0, 1)
    barra_b.tilt(-3000)

def mover_baixo_b():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)
    barra_b.resizemode('user')
    barra_b.shapesize(5, 5, 12)
    barra_b.tilt(3000)

jogo.listen()
jogo.onkeypress(mover_cima_a, "w")
jogo.onkeypress(mover_baixo_a, "s")
jogo.onkeypress(mover_cima_b, "Up")
jogo.onkeypress(mover_baixo_b, "Down")

while True:
    jogo.update()
    bola.setx(bola.xcor() + bola.dx)
    bola.sety((bola.ycor() + bola.dy))

    #bateu na borda de cima volta
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy*= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390 or bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1 # reverte direçao quando alguem ganha



