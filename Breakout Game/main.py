from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from bricks import Bricks
from score_keeper import Scorekeeper
from life_board import Lifekeeper

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle(0)
ball = Ball()
bricks = []
score_keeper = Scorekeeper()
life_keeper = Lifekeeper()

starting_brick_x_position = -354
starting_brick_y_position = 240
for _ in range(11):
    bricks.append(Bricks(starting_brick_x_position, starting_brick_y_position, 1, 3))
    starting_brick_x_position += 70

second_brick_x_position = -375
second_brick_y_position = 210
for _ in range(16):
    bricks.append(Bricks(second_brick_x_position, second_brick_y_position, 1, 2))
    second_brick_x_position += 50

third_brick_x_position = -354
third_brick_y_position = 180
for _ in range(11):
    bricks.append(Bricks(third_brick_x_position, third_brick_y_position, 1, 3))
    third_brick_x_position += 70

fourth_brick_x_position = -374
fourth_brick_y_position = 150
for _ in range(16):
    bricks.append(Bricks(fourth_brick_x_position, fourth_brick_y_position, 1, 2.1))
    fourth_brick_x_position += 50

fifth_brick_x_position = -354
fifth_brick_y_position = 120
for _ in range(11):
    bricks.append(Bricks(fifth_brick_x_position, fifth_brick_y_position, 1, 3))
    fifth_brick_x_position += 70

sixth_brick_x_position = -384
sixth_brick_y_position = 90
for _ in range(16):
    bricks.append(Bricks(sixth_brick_x_position, sixth_brick_y_position, 1, 2.1))
    sixth_brick_x_position += 50


def go_right():
    new_x = paddle.xcor() + 60
    paddle.goto(new_x, paddle.ycor())


def go_left():
    new_x = paddle.xcor() - 60
    paddle.goto(new_x, paddle.ycor())


screen.listen()
screen.onkey(go_right, key='Right')
screen.onkey(go_left, key='Left')

score = 0
live = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.xcor() > 370:
        ball.x_bounce()
    elif ball.xcor() < -370:
        ball.x_bounce()

    if ball.ycor() > 275:
        ball.y_bounce()

    if ball.distance(paddle) < 39:
        ball.y_bounce()

    for c in range(len(bricks)):
        if ball.distance(bricks[c]) < 39:
            ball.y_bounce()
            Bricks.destroy_bricks(bricks[c])
            score += 1
            score_keeper.increase_point()
            if score == 81:
                break
        if ball.distance(bricks[c]) < 39:
            ball.y_bounce()

    if ball.ycor() < -280:
        life_keeper.decrease_life()
        live -= 1
        ball.reset_position()
        if live == 0:
            game_is_on = False
            break

screen.exitonclick()
