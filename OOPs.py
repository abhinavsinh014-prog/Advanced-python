class car:
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

car1 = car(4,4,"disel")
print("Car 1 has {} windows, {} tyres and {} engine.".format(car1.windows,car1.tyres,car1.engine))