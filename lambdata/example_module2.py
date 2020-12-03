"""A collection of classes"""


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for Complex Numbers.
        Complex numbers have a real and imaginary part.
        """
        self.r = realpart
        self.i = imagpart


class Person:
    def __init__(self, name, fave_color):
        """Constructor for Person class"""
        self.name = str(name)
        self.fave_color = str(fave_color)

    def paint_color(self, fave_color_used):
        self.fave_color_used += fave_color
        return "I love this color" + str(fave_color_used)

    def say_name(self, said_name):
        return "My name is" + str(said_name)

class Female:
    """
    A collection of data about characteristics of a female
    """
    def __init__(self, name, fave_color, eye_color, hair_color):
        super().__init__(name, fave_color)
        self.eye_color = str(eye_color)
        self.hair_color = str(hair_color)

    def say_eye_color(self, e_color):
        return "My eyes are the color" + str(e_color)

    def say_hair_color(self, h_color):
        return "My hair is the color" + str(h_color)

if __name__=="__main__":
    person1 = Person("Jessica", "blue")
    person2 = Person("Dave", "green")
    person3 = Person("Valkyrie", "purple")
    print(person1.paint_color())





print("Example 2 worked")