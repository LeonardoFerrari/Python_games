import turtle
import winsound

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
barra_a.shapesize(stretch_wid=5,stretch_len=1)
barra_a.goto(-350,0)

barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("black")
barra_b.penup()
barra_b.shapesize(stretch_wid=5,stretch_len=1)
barra_b.goto(350,0)
#Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color("black")
bola.penup()

# placar
placar_1 = 0
placar_2 = 0
placar = turtle.Turtle()
placar.speed()
placar.color("black")
placar.penup()
placar.hideturtle()
placar.goto(0, 240)
placar.write("Jogador 1: 0    Jogador 2: 0", align="center", font=("Arial", 22, "bold"))

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
        if bola.ycor() > 290:
            bola.sety(290)
        else:
            bola.sety(-290)
        bola.dy *= -1

        # Não é possível utilizar a biblioteca OS de python, uma vez que apenas MacOS e Linux podem usar aplay/afplay
        winsound.PlaySound("bounce.pad.wav", winsound.SND_ASYNC)


    if bola.xcor() > 390 or bola.xcor() < -390:
        if bola.xcor() > 390:
            placar_1 += 1
            placar.clear()
            placar.write("Jogador 1: {}    Jogador 2: {}". format(placar_1,placar_2), align="center", font=("Arial", 22, "bold"))
            winsound.PlaySound("bounce.end.wav", winsound.SND_ASYNC)
        else:
            placar_2 += 1
            placar.clear()
            placar.write("Jogador 1: {}    Jogador 2: {}".format(placar_1, placar_2), align="center", font=("Arial", 22, "bold"))
            winsound.PlaySound("bounce.end.wav", winsound.SND_ASYNC)
        bola.goto(0,0)
        bola.dx *= -1 # reverte direçao quando alguem ganha

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_b.ycor() + 40 and bola.ycor() > barra_b.ycor() - 40):
        bola.setx(340)
        winsound.PlaySound("bounce.pad.wav", winsound.SND_ASYNC)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_a.ycor() + 40 and bola.ycor() > barra_a.ycor() - 40):
        bola.setx(-340)
        winsound.PlaySound("bounce.pad.wav", winsound.SND_ASYNC)
        bola.dx *= -1


