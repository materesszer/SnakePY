import random
from turtle import Turtle


class Food:
    """Food for the snake"""

    def __init__(self):
        self.food = None
        self.create_food()

    def create_food(self):
        if self.food:
            self.food.clear()
            self.food.hideturtle()
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("red")
        self.food.shapesize(1.5, 1.5)
        self.food.goto(random.randint(-250, 250), random.randint(-250, 250))
