from Vehicle import Vehicle
from Engine import Engine


class Car(Vehicle):
    def __init__(self, license_plate, year, Engine: Engine):
        super().__init__(license_plate, year)
        self.Engine = Engine
        self.license_plate = license_plate
        self.year = year

    def calculate_annual_tax(self):
        return f'tax on{self.year} , whit {self.Engine}', self.year // 17
