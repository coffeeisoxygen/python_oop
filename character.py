""""this is a class method for character"""

# pylint: disable=line-too-long


class Bird:
    """ini adalah class untuk bird"""

    species = "burung"  # ini adalah class attribute

    def __init__(self, color, name):  # ini adalah instance attribute
        self.color = color
        self.name = name

    def chirp(self):
        """_summary_: ini adalah method untuk burung berkicau"""
        print("tweet")

    def fly(self, heights=10):
        # kita bisa menetapkan default value di parameter, atau kita bisa memanggil method tanpa parameter
        """_summary_: ini adalah method untuk burung terbang"""
        print(f"{self.name} flies with {heights} height")


my_bird = Bird("merah", "robin")
print(my_bird.color)  # ini adalah instance attribute
print(type(my_bird))  # ini adalah instance type
print(isinstance(my_bird, Bird))  # ini adalah instance type
print(isinstance(my_bird, object))  # ini adalah instance type
print(my_bird.species)  # ini adalah class attribute
