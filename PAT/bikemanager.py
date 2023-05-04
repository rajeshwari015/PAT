class Bike:
    def __init__(self, name, mileage, price, fueltype,cbikes):
        self.name = name
        self.mileage = mileage
        self.price = price
        self.fueltype= fueltype
        self.cbikes=cbikes
    def getBike(self):
        return {
            "name": self.name,
            "mileage": self.mileage,
            "price": self.price,
            "fueltype":self.fueltype,
            "cbikes": self.cbikes,
        }
    def countbikes(self):
        return{
            "count":self.cbikes,
            }

class Manager:
    def __init__(self):
        self.bikes = []
    def add_bike(self, name, mileage, price, fueltype,cbikes):
        bike = Bike(name, mileage, price, fueltype,cbikes)
        self.bikes.append(bike)
    def show_bike(self, name):
        for bike in self.bikes:
            if bike.name == name:
                print(bike.getBike())
                return
        return None
    def buy_bike(self, bike_name):
        for bike in self.bikes:
            if bike.name == bike_name:
                bike.cbikes-=1
                #self.bikes.remove(bike)
                return
    def no_bikes(self,name):
        for bike in self.bikes:
            if bike.name!=name:
                print("The bike is not available")
                return 
    def display_noofbikes(self,name):
        for bike in self.bikes:
            if bike.name==name:
                print(bike.countbikes())
                return
        return None
    def print_array(self):
        for bike in self.bikes:
            print(bike.getBike())


manager = Manager()
manager.add_bike("classic", 33, "2 lakhs","petrol",3)
manager.add_bike("thunderbird", 35, "3 lakhs","diesel",4)
manager.add_bike("meteor", 30, "3.6 lakhs","petrol",5)
manager.add_bike("herohonda",36,"1 lakh","petrol",6)

#manager.print_array()
manager.buy_bike("herohonda")
manager.display_noofbikes("herohonda")
manager.no_bikes("gt650")
manager.show_bike("classic")
