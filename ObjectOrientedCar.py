import sys


carList = {}

class Car:
    car_make = "Make"
    car_model = "Model"
    car_year = "Year"

    def setMake(self, Make):
        self.Make = Make
    def setModel(self, Model):
        self.Model = Model
    def setYear(self, Year):
        self.Year = Year
    
    def getYear(self):
        return self.Year
    def getModel(self):
        return self.Model
    def getMake(self):
        return self.Make
    
def main():
    
    SuperCar = Car()
    superwhile = 0
    while superwhile != -1:
        userMake = input("Please input the make for the car: ")
        userModel = input("Please input the model for the car: ")
        userYear = input("Please input a year for the car: ")

        SuperCar.setMake(userMake)
        SuperCar.setModel(userModel)
        SuperCar.setYear(userYear)

        tempList = [SuperCar.getMake(), SuperCar.getModel(), SuperCar.getYear()]
        carList[superwhile] = tempList

        for key, value in carList.items():
            print("Car: ")
            for values in value:
                print(values)
        
        superwhile = superwhile + 1

main()
