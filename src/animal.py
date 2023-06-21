from color import Color, print_styled

class Animal:
    """
    Represents an ordinary animal with legs and eyes.
    """

    total_animals = 0

    def __init__(self, number_of_legs, number_of_eyes):
        """
        Initializes an animal with the given number of legs and eyes.
        """

        self._number_of_legs = number_of_legs
        self._number_of_eyes = number_of_eyes
        Animal.total_animals += 1

    @property
    def average_speed(self):
        """
        Calculates and returns the average speed of the animal.
        """

        return self._number_of_legs * 5

    def breathe(self):
        """
        Performs the breathing action for the animal.
        """

        print_styled("The Animal is breathing.", Color.YELLOW)

    def walk(self):
        """
        Performs the walking action for the animal.
        """

        print_styled(f"Walking with {self._number_of_legs} legs.", Color.YELLOW)

    def summary(self):
        """
        Prints a summary of the animal's attributes.
        """

        print_styled(f"This is an instance of [Animal]. It has {self._number_of_legs} legs and {self._number_of_eyes} eyes.", Color.YELLOW)
        print_styled(f"The average speed of this animal is {self.average_speed} units per minute.", Color.YELLOW)
