import turtle

# Configurações da janela
janela = turtle.Screen()
janela.title("Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("red")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("blue")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = 0.1

# Placar

Azul = 0
Vermelho = 0

placar = turtle.Turtle()
placar.write(f"Azul {Azul} // Vermelho {Vermelho}", center, comic-sans)
placar.color('white')
placar.
placar.goto(750,300)


# Funções de movimento
def raquete_a_cima():
    y = raquete_a.ycor()
    y += 25
    raquete_a.sety(y)

def raquete_a_baixo():
    y = raquete_a.ycor()
    y -= 25
    raquete_a.sety(y)

def raquete_b_cima():
    y = raquete_b.ycor()
    y += 25
    raquete_b.sety(y)

def raquete_b_baixo():
    y = raquete_b.ycor()
    y -= 25
    raquete_b.sety(y)

#Pause

paused = False

def unpause():
    print("unpause() called")
    global paused
    paused = False

def pause():
    print("pause() called")
    global paused
    paused = True
    pausing()

def pausing():
    if paused:
        turtle.ontimer(pausing, 6000)

# Teclado

janela.listen()
janela.onkeypress(pause , "p")
janela.onkeypress(unpause , "o")
janela.onkeypress(raquete_a_cima, "w")
janela.onkeypress(raquete_a_baixo, "s")
janela.onkeypress(raquete_b_cima, "Up")
janela.onkeypress(raquete_b_baixo, "Down")

# Loop do jogo

while True:
    janela.update()
    
        # Move a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

        # Verifica se a bola atingiu as bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1


    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    