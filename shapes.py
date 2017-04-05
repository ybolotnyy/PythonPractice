import turtle

class Shape:
    shapesCount = 0

    def displayCount(self):
        print("total %d shapes exist" % Shape.shapesCount)

    def __init__(self, corners):
        self.cornersTotal = corners
        Shape.shapesCount += 1
        print ("%d-corners shape created" % corners)
        self.displayCount()


def initTurtle(shape, color, speed):
    brad = turtle.Turtle()
    brad.shape(shape)
    brad.color(color)
    brad.speed(speed)
    return brad

def draw_shape(total_sides, total_figurines):

    brad = initTurtle("turtle", "yellow", 100)

    window = turtle.Screen()
    window.bgcolor("red")


    for i in range(0, total_figurines):
        angle_diff = int(360/total_figurines)
        brad.right(angle_diff)
        for i in range(0, total_sides):
            brad.forward(100)
            brad.right(int(360 / total_sides))

    window.exitonclick()

def draw_shapes(total_sides, total_figurines):

    brad = initTurtle("turtle", "yellow", 100)
    window = turtle.Screen()
    window.bgcolor("red")


    # for i in range(0, total_figurines):
    #     angle_diff = int(360/total_figurines)
    #     brad.right(angle_diff)
    #     for i in range(0, total_sides):
    #         brad.forward(100)
    #         brad.right(int(360 / total_sides))

    window.exitonclick()

triangle = Shape(3)
square = Shape(4)
pentagon = Shape(5)
hexagon = Shape(6)





draw_shape(4,10)