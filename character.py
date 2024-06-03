""""this is a class method for character"""


class Bird:
    """ini adalah class untuk bird"""

    def __init__(self, color):
        self.color = color


my_bird = Bird("merah")
print(my_bird.color)  # ini adalah instance attribute
print(type(my_bird))  # ini adalah instance type
print(isinstance(my_bird, Bird))  # ini adalah instance type
print(isinstance(my_bird, object))  # ini adalah instance type
