from tkinter import messagebox
from turtle import Turtle, Screen

from food import Food
from score import Score


class Snake:
    """Contains the logic and attributes for the player's snake"""

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.cubes = self.setup_snake()
        self.head = self.cubes[0]
        self.current_direction = "Right"

    def setup_snake(self):
        body = []
        for position in self.positions:
            cube = Turtle("square")
            cube.color("white")
            cube.penup()
            cube.goto(position)
            body.append(cube)
        return body

    def enlarge_snake(self, tail_position):
        cube = Turtle("square")
        cube.color("white")
        cube.penup()
        cube.goto(tail_position)
        self.cubes.append(cube)

    def move(self):
        for i in range(len(self.cubes) - 1, 0, -1):
            new_x = self.cubes[i - 1].xcor()
            new_y = self.cubes[i - 1].ycor()
            self.cubes[i].goto(new_x, new_y)
        self.set_snake_direction()
        self.head.forward(20)

    def set_snake_direction(self):
        if self.current_direction == "Up":
            self.head.setheading(90)
        elif self.current_direction == "Down":
            self.head.setheading(270)
        elif self.current_direction == "Left":
            self.head.setheading(180)
        elif self.current_direction == "Right":
            self.head.setheading(0)


class Collisions:
    """Collision handling"""

    def __init__(self, snake, food, score):
        self.snake = snake
        self.food = food
        self.score = score

    def handle_food_collision(self):
        if abs(self.snake.head.xcor() - self.food.food.xcor()) <= 25 and abs(self.snake.head.ycor() - self.food.food.ycor()) <= 25:
            self.food.create_food()
            self.score.increase_score()
            self.snake.enlarge_snake(self.snake.cubes[-1].pos())

    def handle_tail_collision(self):
        for segment in self.snake.cubes[1:]:
            if self.snake.head.distance(segment) < 10:
                messagebox.showinfo(
                    "Game Over", f"You lost!\nScore: {self.score.score}")
                return True
        return False

    def handle_wall_collision(self):
        if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or \
           self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
            messagebox.showinfo(
                "Game Over", f"You lost!\nScore: {self.score.score}")
            return True


class GameScreen:
    """Game screen ties together the whole program"""

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.snake = Snake()
        self.score = Score()
        self.food = Food()
        self.collisions = Collisions(self.snake, self.food, self.score)

        self.setup_controls()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.set_direction("Up"), "Up")
        self.screen.onkey(lambda: self.set_direction("Down"), "Down")
        self.screen.onkey(lambda: self.set_direction("Left"), "Left")
        self.screen.onkey(lambda: self.set_direction("Right"), "Right")

    def set_direction(self, direction):
        if (direction == "Up" and self.snake.current_direction != "Down") or \
           (direction == "Down" and self.snake.current_direction != "Up") or \
           (direction == "Left" and self.snake.current_direction != "Right") or \
           (direction == "Right" and self.snake.current_direction != "Left"):
            self.snake.current_direction = direction

    def game_loop(self):
        if self.collisions.handle_tail_collision() or self.collisions.handle_wall_collision():
            return
        self.collisions.handle_food_collision()
        self.snake.move()
        self.screen.update()
        self.screen.ontimer(self.game_loop, 100)

    def start_game(self):
        self.setup_controls()
        self.game_loop()
        self.screen.mainloop()


game_screen = GameScreen()
game_screen.start_game()
