import turtle


def draw_sun() -> None:
    """Функція, яка малює сонце з променями."""
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("orange", "yellow")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    for _ in range(12):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.forward(100)
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.right(30)


def write_text(message: str) -> None:
    """Функція, яка друкує текстове повідомлення над солнцем."""
    turtle.penup()
    turtle.goto(-70, 120)
    turtle.color("red")
    turtle.pendown()
    turtle.write(message, font=("Arial", 20, "bold"))


def main() -> None:
    """Основна функція, яка запускає малювання."""
    turtle.speed(5)
    draw_sun()
    write_text("Hello, world!")
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
