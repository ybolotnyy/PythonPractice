class Parent():
    def __init__(self, last_name, first_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.first_name = first_name
        self.eye_color = eye_color

    def print_info(self):
        print("last name - " + self.last_name)
        print("first name - " + self.first_name)
        print("eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, first_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, first_name, eye_color)
        self.number_of_toys = number_of_toys

    def print_info(self):
        print("last name - " + self.last_name)
        print("first name - " + self.first_name)
        print("eye color - " + self.eye_color)
        print("Number of toys - %d" % self.number_of_toys)

will_smith = Parent("Will", "Smith", "blue")
will_smith.print_info()

bonnie_smith = Child("Bonnie", "Smith", "grey", 3)
bonnie_smith.print_info()