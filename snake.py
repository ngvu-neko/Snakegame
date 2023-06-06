from turtle import Turtle

starting_position = [(0,0),(-20,0),(-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    # Hamf nayf là hàm khi khối 0 chạm Food thì sẽ thêm 1 khối ở vị trí cuối cùng của Snake
    def extend_snake(self):
        self.add_segment(self.segments[-1].position()) # hàm position là hàm trả về vị trí hiện tại của turtle

    def move(self):
        for seg_num in range(len(self.segments)-1, 0 , -1):
            new_x = self.segments[seg_num -1 ].xcor()
            new_y = self.segments[seg_num -1 ].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # di chuyển khối đầu ( khối thứ 0 )
        self.segments[0].forward(MOVE_DIS)

    def reset(self):

        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

