from ElectricMixin import ElectricMixin
from LuxuryMixin import LuxuryMixin
from Car import Car
class ElectricCar(ElectricMixin,LuxuryMixin,Car):
    def calculate_annual_tax(self):
        return f'the tax for electric car is 250 usd$'