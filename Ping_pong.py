import turtle
STEP = 20


class Bat(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.bats = []
        self.create_bat((-380, 0))
        self.create_bat((380, 0))
        self.break_screen()

    def break_screen(self):
        t = turtle.Turtle()
        t.pensize(5)
        t.color('white')
        t.penup()
        t.goto(0, -380)
        t.lt(90)
        t.speed(0)
        while t.ycor() < 380:
            t.pendown()
            t.fd(50)
            t.up()
            t.fd(30)
        turtle.hideturtle()

    def create_bat(self, position):
        t = turtle.Turtle(shape='square')
        t.shapesize(stretch_wid=4, stretch_len=1)
        t.color('white')
        t.penup()
        t.goto(position)
        self.bats.append(t)

    def move_up(self):
        y_pos = self.bats[0].ycor() + STEP
        self.bats[0].goto(self.bats[0].xcor(), y_pos)

    def move_DOWN(self):
        y_pos = self.bats[0].ycor() - STEP
        self.bats[0].goto(self.bats[0].xcor(), y_pos)

    def move_left(self):
        y_pos = self.bats[1].ycor() - STEP
        self.bats[1].goto(self.bats[1].xcor(), y_pos)

    def move_right(self):
        y_pos = self.bats[1].ycor() + STEP
        self.bats[1].goto(self.bats[1].xcor(), y_pos)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.color('blue')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        y_pos = self.ycor() + self.y_move
        x_pos = self.xcor() + self.x_move
        self.goto(x_pos, y_pos)

    def ball_bouncey(self):
        self.y_move *= -1

    def ball_bouncex(self):
        self.x_move *= -1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_bouncex()
        self.move_speed = 0.1


class Score_Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.rscore = 0
        self.lscore = 0
        self.penup()

        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-300, 280)
        self.write(f'player1:{self.lscore}', align='center', font=('courier', 00, 'normal'))
        self.color('pink')
        self.goto(300, 280)
        self.write(f'player2:{self.rscore}', align='center', font=('courier', 00, 'normal'))

    def score_increasel(self):
        self.lscore += 1
        self.update_score()

    def score_increaser(self):
        self.rscore += 1
        self.update_score()