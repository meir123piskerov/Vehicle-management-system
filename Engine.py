class Engine:
    def __init__(self, fuel_type=str, horsepower=int):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __str__(self):
        return self.horsepower