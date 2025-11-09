from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, license_plate, year):
        self.__year = year
        self.__license_plate = license_plate

    def get__plate_license(self):
        return self.__license_plate

    def year_get(self):
        return self.__year

    def set__plate_license(self, set):
        if set:
            self.__license_plate =set

    def set__year(self, set):
        if set:
            self.__year = set

    @abstractmethod
    def calculate_annual_tax(self):
        pass
