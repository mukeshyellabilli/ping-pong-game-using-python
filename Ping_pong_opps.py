import turtle
from ping_pong_oops import Bat, Ball, Score_Board
import time
s = turtle.Screen()
STEP = 20
s.setup(width=800, height=600)
turtle.bgcolor('black')
s.title('MY PONG GAME')
s.tracer(0)

b = Bat()
l, r = b.bats
g = Ball()
score = Score_Board()

s.listen()
s.onkeypress(key='Up', fun=b.move_up)
s.onkeypress(key='Down', fun=b.move_DOWN)
s.onkeypress(key='Left', fun=b.move_left)
s.onkeypress(key='Right', fun=b.move_right)

is_game_on = True
while is_game_on:
    time.sleep(g.move_speed)
    s.update()
    g.move()
# detect collision with walls
    if g.ycor() > 280 or g.ycor() < -280:
        g.ball_bouncey()
# detect collision with bats
    if (g.distance(r) < 50 and g.xcor() > 320) or (g.distance(l) < 50 and g.xcor() < -320):
        g.ball_bouncex()
    else:
        # right bat misses
        if g.xcor() > 420:
            g.reset_position()
            score.score_increasel()
        # left bat misses
        if g.xcor() < -420:
            g.reset_position()
            score.score_increaser()

s.exitonclick()