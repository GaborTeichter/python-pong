import turtle

class Ablak():

    def __init__(self, ablak, szelesseg = 800, magassag = 600, hatterszin = "black", cim = "PONG"):

        self.ablak = ablak
        self.ablak.setup(width=800, height=600)
        self.ablak.bgcolor(hatterszin)
        self.ablak.title(cim)
        self.ablak.tracer(0)
        self.ablak.listen()

class Player():

    def __init__(self, turtle, sebesseg = 0, forma = "square", szelesseg = 5, hosszusag = 1, szin = "white", koordinataX = -350, koordinataY = 0, fel = "w", le = "s"):

        self.player = turtle
        self.player.speed(sebesseg)
        self.player.shape(forma)
        self.player.shapesize(stretch_wid=szelesseg, stretch_len=hosszusag)
        self.player.color("green")
        self.player.penup()
        self.player.goto(koordinataX, koordinataY)
        self.fel = fel
        self.le = le
        self._pontszam = 0

        @property
        def pontszam(self):

            return self._pontszam

        @staticmethod
        def pontszam_kiirasa(players):

            pontszam = turtle.Turtle()
            pontszam.speed(0)
            pontszam.color('white')
            pontszam.penup()
            pontszam.hideturtle()
            pontszam.goto(0, 260)
            pontszam.write(f"Player A: {players[0].pontszam}  Player B: {players[1].pontszam}", align='center', font=('Courier', 24, 'bold'))

        def player_up(self):
            y = self.player.ycor()
            y += 30
            self.player.sety(y)
        
        def player_down(self):
            y = self.player.ycor()
            y -= 30
            self.player.sety(y)

        def control(self, ablak):
            ablak.onkey(player_up, self.fel)
            ablak.onkey(player_down, self.le)


class Ball():

    bal_pontszam = 0
    jobb_pontszam = 0

    def __init__(self, ball, sebesseg = 0, forma = "circle", szin = "white", koordinataX = 0, koordinataY = 0, valtozasX = 1, valtozasY = -1):

        self.ball = turtle.Turtle()
        self.ball.speed(sebesseg)
        self.ball.shape(forma)
        self.ball.color(szin)
        self.ball.penup()
        self.ball.goto(koordinataX, koordinataY)
        self.ball.valtozasX = valtozasX
        self.ball.valtozasY = valtozasY

    def move(self):
        # Moving Ball
        self.ball.setx(self.ball.xcor() + self.ball.valtozasX)
        self.ball.sety(self.ball.ycor() + self.ball.valtozasY)

        # tetejéről pattanjon vissza
        if self.ball.ycor() > 288:
            self.ball.sety(288) 
            self.ball.valtozasY *= -1

        # aljáról pattanjon vissza
        if self.ball.ycor() < -288:
            self.ball.sety(-288) 
            self.ball.valtozasY *= -1

        # jobb oldal érintése
        if self.ball.xcor() > 388:
            self.ball.goto(0,0) 
            self.ball.valtozasY *= -1
            bal_pontszam += 1

        # bal oldal érintése
        if self.ball.xcor() < -388:
            self.ball.goto(0,0) 
            self.ball.valtozasY *= -1
            jobb_pontszam += 1
        


ablak = Ablak(turtle.Screen())
ball = Ball(turtle.Turtle())

left_player = Player(turtle.Turtle())
right_player = Player(turtle.Turtle(), koordinataX=350, koordinataY=0) 

while True:    
    # screen update
    ablak.ablak.update()
    ball.move()