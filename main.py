from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SNAKE_SPEED = 0.1

screen = Screen()
screen.setup(width = 600, height = 600 )
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


snake = Snake() 
food = Food()
score = ScoreBoard()

game_is_on = True
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left,  "a")
# screen.onkey()

while game_is_on:
	screen.update()
	time.sleep(SNAKE_SPEED)
	snake.move()

	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		score.increase_score()

	#Detect wall collision
	boundary = snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280

	if boundary:
		score.reset()
		snake.reset()



	#Detect tail collision
	for segment in snake.segments[1:]:
		
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()
			













		































screen.exitonclick()