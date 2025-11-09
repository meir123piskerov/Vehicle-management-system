from Vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, license_plate, year,max_load):
        super().__init__(license_plate,year)
        self.max_load = max_load

    def calculate_annual_tax(self):
        return f'for max load of {self.max_load}, the tax is {self.max_load * 2.5}'