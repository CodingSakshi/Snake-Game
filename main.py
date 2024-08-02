from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor(40/255, 99/255, 68/255)
screen.title("My snake game")
screen.tracer(0)  # Turn off automatic screen updates

snake = Snake()
food = Food()
score = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(snake.up, "Up")  # snake.up function will get triggered when will use up key
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # To detect collission with food

    if snake.head.distance(food) < 25:    # We can't write snake.distance, coz snake is made of turtle n its starting is head, less that 15 coz 10 is size of food and 5 is buffer
        food.refresh()
        snake.extend()
        score.increase_score()

    # To detect collission with wall
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset_snake()
    
    # To detect collission with snake
    # We will traverse all segments and check the distance of head from each of them if they are less than 10, coz 10 is the size of our block, so ofcourse its a collision
    
    for block in snake.blocks[1: ]:     # Ofcourse the distance of head from head will ofcourse less than 10 and therefore there will be collission so pass
        if snake.head.distance(block) < 10:
            score.reset()
            snake.reset_snake()
            


screen.exitonclick()