from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   # Constants
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    
    def __init__(self) -> None:
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def extend(self):
        self.add_block(self.blocks[-1].position())
        
    def move(self):
        # Move each block to the position of the previous block
        for i in range(len(self.blocks) - 1, 0, -1):  # start, stop, step
            new_x = self.blocks[i - 1].xcor()
            new_y = self.blocks[i - 1].ycor()
            self.blocks[i].goto(new_x, new_y)
        # Move the first block to the new position (head movement)
        self.blocks[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for block in self.blocks:
            block.goto(1200, 1200)  # Move the block out of the screen
        self.blocks.clear()
        self.__init__()

    def left(self):
        if self.head.heading != LEFT:
            self.head.setheading(LEFT)
    
    def up(self):
        if self.head.heading != UP:
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading != RIGHT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading != DOWN:
            self.head.setheading(DOWN)

    

        
