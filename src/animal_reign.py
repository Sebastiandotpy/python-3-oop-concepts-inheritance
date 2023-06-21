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

        print_styled("The Animal is breathing.", Color.ACTION)

    def walk(self):
        """
        Performs the walking action for the animal.
        """

        print_styled(f"Walking with {self._number_of_legs} legs.", Color.ACTION)

    def summary(self):
        """
        Prints a summary of the animal's attributes.
        """

        print_styled(f"This is an instance of [Animal]. It has {self._number_of_legs} legs and {self._number_of_eyes} eyes.",
                     Color.ANIMAL_TITLE)
        print_styled(f"The average speed of this animal is {self.average_speed} units per minute.", Color.ANIMAL_TITLE)


class Dog(Animal):
    """
    Represents a dog, which is a type of animal.
    """

    def __init__(self, number_of_legs, number_of_eyes, breed):
        """
        Initializes a dog with the given number of legs, eyes, and breed.
        """

        super().__init__(number_of_legs, number_of_eyes)
        self._breed = breed

    def bark(self):
        """
        Performs the barking action for the dog.
        """

        print_styled("Dogs love to bark.", Color.ACTION)

    def summary(self):
        """
        Prints a summary of the dog's attributes.
        """

        super().summary()
        print_styled(f"This is an instance of [Dog]. It has {self._number_of_legs} legs and {self._number_of_eyes} eyes.",
                     Color.ANIMAL_TITLE)
        print_styled(f"The average speed of this dog is {self.average_speed} units per minute.", Color.ANIMAL_TITLE)
        print_styled(f"{self._breed} show their beautiful fur while running.", Color.ANIMAL_TITLE)
        print_styled("Dogs love to breathe with their mouths open.", Color.ACTION)
        print_styled("Dogs love to bark.", Color.ACTION)


def main():
    print_styled("╭─────────────────────────────────────────────────╮", Color.ANIMAL_SUMMARY)
    print_styled("│                 Animal Reign                    │", Color.ANIMAL_SUMMARY)
    print_styled("╰─────────────────────────────────────────────────╯", Color.ANIMAL_SUMMARY)

    animals = [
        Animal(2, 2),
        Dog(4, 2, "German Shepherd"),
        Dog(4, 2, "German Shepherd")
    ]

    for animal in animals:
        print_styled("┌──────────────────────────────┐", Color.ANIMAL_SUMMARY)
        animal.summary()
        print_styled("│           Actions            │", Color.ANIMAL_SUMMARY)
        animal.breathe()
        animal.walk()
        if isinstance(animal, Dog):
            animal.bark()
        print_styled("└──────────────────────────────┘", Color.ANIMAL_SUMMARY)


if __name__ == "__main__":
    main()
