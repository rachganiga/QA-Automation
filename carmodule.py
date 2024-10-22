class CarApp:
    ''' Car Application for Customer'''

    def __init__(self,name):
        '''Initialisation of CarApp class'''
        self.name = name #object variable
        print("Car Name:",name)

        
    def info(self):
        '''Car Information Method'''
        print("It`s Audi Car",self.name)


if __name__ == '__main__':
    AudiCar = CarApp("Audi Car Name")
    print(AudiCar.__doc__)
    AudiCar.info()