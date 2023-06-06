from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width = 600   , height = 600)
screen.bgcolor('black')
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True
# Thuật toán di chuyển của rắn Là các khối ở sau cùng sẽ di chuyển theo khối trước đó
# Ví dụ , con snake có 8 khối thì khối cuối(8) sẽ di chuyển đến vị trí của khối thứ 7 , và lặp lại
# Sau đó ta chỉ việc di chuyển khối đầu tiền là OK
while game_is_on:
    screen.update() #update frame lên màn hình screen sau khi thay đổi
    time.sleep(0.1)
    # đây là câu lệnh làm cho sác khối cuối (n) di chuyển đến vị trí của khối thứ (n - 1)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15 :
        # refresh lại vị trí của food khi khoảng cách của food và đầu rắn < 15
        food.refresh()
        snake.extend_snake()
        # tăng giá trị của socre
        score.increase_socre()

    # Detext collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() < -290:
        score.reset_game()
        snake.reset()

    # Detect collision with tail

    for segment in snake.segments[-1:]:
        # vif snake.head là vị trí đầu và segment có cả vị trí đầu nên chúng ta cần pass
        # trường hợp snake.head == segment

        if snake.head.distance(segment) < 10 :
            score.reset_game()
            snake.reset()




screen.exitonclick()
