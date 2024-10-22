class CarApp:
    ''' Car Application for Customer'''

    def __init__(self,name):
        '''Initialisation of CarApp class'''
        self.name = name #object variable
        print("Car Name:",name)

        
    def info(self):
        '''Car Information Method'''
        print("It`s Audi Car",self.name)


AudiCar = CarApp("Audi Car Name")
print(AudiCar.__doc__)
