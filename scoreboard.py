from turtle import Turtle
from snake import Snake
ALIGN  = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    # đây là 1 ví dụ cho class inheritance
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        with open('score.txt' ) as data:
            self.hightscore = int(data.read())
        self.update_scoreboard()
         # thường setup cả các hàm mà thay đổi liên tục
        # vẽ lại bảng điểm sau mỗi lần ăn đc food
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} , High score : {self.hightscore}", False, align= ALIGN , font = FONT)

    def reset_game(self):
        if self.score > self.hightscore:
            self.hightscore = self.score
        with open('score.txt' ,mode= 'w') as data:
            data.write(f"{self.hightscore}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, align= ALIGN , font = FONT)

    def increase_socre(self):
        self.score += 1
        self.update_scoreboard()

