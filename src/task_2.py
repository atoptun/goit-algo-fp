import turtle
import math
from rgb_gradient import get_linear_gradient


def draw_pythagoras_tree(t: turtle.Turtle, x, y, size, angle: float, level: int, colors: list):
    """Recursively draws a Pythagoras tree"""
    if level == 0:
        return

    color = colors[level - 1]
    t.color(color)
    t.pensize(max(1, level))

    x_top = x + size * math.cos(math.radians(angle))
    y_top = y + size * math.sin(math.radians(angle))

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x_top, y_top)

    new_size = size / math.sqrt(2)

    draw_pythagoras_tree(t, x_top, y_top, new_size, angle + 45, level - 1, colors)
    draw_pythagoras_tree(t, x_top, y_top, new_size, angle - 45, level - 1, colors)


def main():
    level = int(input("Enter recursion level (e.g., 5-10): "))
    # level = 5
    size = 200

    intermediate_colors = ['#228b22', '#8b4513']
    colors = get_linear_gradient(colors=intermediate_colors, nb_colors=level, return_format='hex')

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    
    draw_pythagoras_tree(t, 0, -300, size, 90, level, colors)
    turtle.done()


if __name__ == "__main__":
    main()
