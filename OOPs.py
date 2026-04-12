from os import name


class car:
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    def drive(self):
        print("Car have a {} engine".format(self.engine))

# car1 = car(4,4,"disel")
# print("Car has {} windows, {} tyres and {} engine.".format(car1.windows,car1.tyres,car1.engine))
# print(f"Car has {car1.windows} windows, {car1.tyres} tyres and {car1.engine} engine.")
# car1.drive()


class animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
        


    def make_sound(self):
        print("{} makes a sound".format(self.name))

animal1 = animal("Dog")
animal1.make_sound()