from dog import Dog
from color import Color, print_styled

class GermanShepard(Dog):
    """
    Represents a German Shepard, which is a type of dog.
    """

    def walk(self):
        """
        Performs the walking action for the German Shepard.
        """

        super().walk()
        print_styled("German Shepards show their beautiful fur while running.", Color.ANIMAL_SUMMARY)
