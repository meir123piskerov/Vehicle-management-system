from Car import *
from ElectricCar import *
from truck import *

if __name__ == "__main__":
    engine = Engine("95",1600)
    car = Car("209-12-123", "2019", engine)
    engine_electric = Engine('electric',"200")
    BYD = ElectricCar("234-65-436",'2021',engine_electric)
    volvo_truck = Truck('23-234-43',2013,5500)
    vehicles = [car,BYD,volvo_truck]
    for i in vehicles:
        print(i.calculate_annual_tax())

    car.set__plate_license("345-78-983")
    print(car.get__plate_license())

    print(BYD.charge())
    print(BYD.get_luxury_features())

