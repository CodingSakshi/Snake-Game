from turtle import Turtle, Screen
from color import color_list
import turtle
import random

class Wall:
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.penup()
        self.timmy.goto(-300, -300)
        self.timmy.speed("fastest")
        for _ in range(4):
            self.forward(24)
            self.new_line()

    def forward(self, distance):
        distance_covered = 0
        while distance_covered <= 580:  # Adjusted to cover 600 pixels for the square border
            color = random.choice(color_list)
            fill_color = "#%02x%02x%02x" % color
            self.timmy.fillcolor(fill_color)
            self.timmy.pencolor(fill_color)
            self.timmy.shape("square")
            self.timmy.stamp()
            self.timmy.forward(distance)
            distance_covered += distance

    def new_line(self):
        self.timmy.left(90)


