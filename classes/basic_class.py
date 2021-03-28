class Car:
    """
    class definition
    """

    def __init__(self, make, model, year, miles):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def __str__(self):
        return f"{self.make} {self.model}, {self.year}, {self.miles}"

    def __repr__(self):
        return f"{self.make} {self.model}, {self.year}, {self.miles}"

    def drive(self, mph):
        return f"{self.make} {self.model}, {self.year}, {mph}"


def main():
    car = Car("Mini", "BMW", 2009, 1000)
    print(repr(car))
    print(str(car))
    print(car.drive(100))


if __name__ == '__main__':
    main()
