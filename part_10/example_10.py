import turtle


def draw_circle(color: str, x: int, y: int, radius: int) -> None:
    """
    Draws a filled circle with the given color and radius at the specified coordinates.

    :param color: Color of the circle.
    :param x: X-coordinate of the circle's center.
    :param y: Y-coordinate of the circle's center.
    :param radius: Radius of the circle.
    """
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_b() -> None:
    """
    Draws the letter 'b' as part of the Beats Audio logo.
    """
    turtle.penup()
    turtle.goto(-22, 88)
    turtle.pendown()
    turtle.color("white")
    turtle.pensize(20)
    turtle.right(90)
    turtle.forward(100)
    turtle.circle(25, 180)
    turtle.forward(25)
    turtle.circle(25, 180)
    turtle.forward(25)


def main() -> None:
    """
    Main function to draw the Beats Audio logo using the turtle module.
    """
    turtle.speed(3)
    turtle.bgcolor("black")

    draw_circle("red", 0, 0, 100)  # Рисуем большой красный круг
    draw_b()  # Рисуем белую букву "b"

    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
