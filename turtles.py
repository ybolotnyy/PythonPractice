import turtle


def draw_square(total_sides, total_figurines):
    window = turtle.Screen()
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)


    for i in range(0, total_figurines):
        angle_diff = int(360/total_figurines)
        brad.right(angle_diff)
        for i in range(0, total_sides):
            brad.forward(100)
            brad.right(int(360 / total_sides))


    window.exitonclick()


draw_square(4,30)