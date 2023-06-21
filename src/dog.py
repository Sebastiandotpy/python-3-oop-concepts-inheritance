from animal import Animal
from color import Color, print_styled

class Dog(Animal):
    """
    Represents a dog, which is a type of animal.
    """

    def __init__(self, number_of_legs, number_of_eyes):
        """
        Initializes a dog with the given number of legs and eyes.
        """
        super().__init__(number_of_legs, number_of_eyes)

    def bark(self):
        """
        Performs the barking action for the dog.
        """
        print("Dogs love to bark.")

    def summary(self):
        """
        Prints a summary of the dogs attributes.
        """
        print_styled("This is an instance of [Dog].", Color.CYAN)
        print(f"It has {self._number_of_legs} legs and {self._number_of_eyes} eyes.")
        print(f"The average speed of this dog is {self.average_speed} units per minute.")
        print_styled("German Shepherds show their beautiful fur while running.", Color.MAGENTA)
