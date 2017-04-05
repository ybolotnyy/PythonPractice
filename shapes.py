import turtle

class Shape:
    shapesCount = 0

    def displayCount(self):
        print("total %d shapes exist" % Shape.shapesCount)

    def __init__(self, corners):
        self.cornersAmount = corners
        Shape.shapesCount += 1
        print ("%d-corners shape created" % corners)
        self.displayCount()


def initTurtle(shape, color, speed):
    brad = turtle.Turtle()
    brad.shape(shape)
    brad.color(color)
    brad.speed(speed)
    return brad

def draw_shape(shape, shapesCount):

    brad = initTurtle("turtle", "yellow", 100)
    cornersQuantity = shape.cornersAmount

    for i in range(0, shapesCount):
        angle_diff = int(360/shapesCount)
        brad.right(angle_diff)
        for i in range(0, cornersQuantity):
            brad.forward(100)
            brad.right(int(360 / cornersQuantity))


triangle = Shape(3)
square = Shape(4)
pentagon = Shape(5)
hexagon = Shape(6)

window = turtle.Screen()
window.bgcolor("red")

draw_shape(triangle, 5)
draw_shape(square, 5)
draw_shape(pentagon, 5)
draw_shape(hexagon, 5)

window.exitonclick()
