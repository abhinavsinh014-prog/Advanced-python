class car:
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

car1 = car(4,4,"disel")
print(car1.windows)
print(car1.tyres)
print(car1.engine)