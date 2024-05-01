from cars_packages.car_module_two import UseColor
class Car:

    def __init__(self, name, type, country):
        self.name = name
        self.type = type
        self.country = country

    def drive(self):
        return 'I love to drive this car'
    