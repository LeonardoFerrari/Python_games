import turtle

jogo = turtle.Screen()
jogo.title("Teste")
jogo.bgcolor('pink')
jogo.setup(width=800, height=600)
jogo.tracer()

# Barra
barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("black")
barra_a.penup()
barra_a.shapesize(7,1,0)
barra_a.goto(-350,0)

barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("black")
barra_b.penup()
barra_b.shapesize(7,1,0)
barra_b.goto(350,0)
#Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color("black")
bola.penup()

# Colocar opção para escolher velocidade da bola depois, 2/-2 default
bola.dx = 2.5
bola.dy = -2.5

# Funções

def mover_cima_a():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def mover_baixo_a():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def mover_cima_b():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def mover_baixo_b():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)

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
    if bola.ycor() > 290 or bola.ycor() < -290:
        bola.dy *= -1

    if bola.xcor() > 390 or bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1 # reverte direçao quando alguem ganha

    if bola.xcor() > 340 and (bola.ycor() < barra_a.ycor() + 40 and bola.ycor() > barra_a.ycor() - 40):
        bola.dx *= -1



