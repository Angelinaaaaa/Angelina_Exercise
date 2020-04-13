class Person:
    """ Create a Person class
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is
        health_points (int): Out of 100 (everyone starts at 100)
    """

    def __init__(self, name, height, strength):
        """ Create a person object
        Args:
            height: in cm
            name: First and last
            strength: How strong the person is
        """
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100

    def __str__(self) -> str:
        return "{0}, hp: {1}".format(self.name, self.health_points)

    def introduce(self) -> None:
        """Make the one introduce oneself """
        print("Hello, my name is {0}".format(self.name))

    def punch(self, person) -> None:
        """Punch a person
        Drop the person (being punched)'s health points
        Args:
            person: The Person(class) that is being punched
        """
        person.health_points -= 10

    def eat(self) -> None:
        """Restore the health points back to 100"""
        self.health_points = 100


def main():
    barney = Person("Barney", 170, 1)
    angelina = Person("AN", 200, 1)

    # call introduce function
    barney.introduce()
    angelina.introduce()

    # auto call _str_ function
    print(barney)
    print(angelina)

    # call punch function
    barney.punch(angelina)

    # auto call _str_ function
    print(barney)
    print(angelina)

    # call eat function
    angelina.eat()
    print(angelina)

if __name__ == "__main__":
    main()