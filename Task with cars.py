class Automobile:

    def __init__(self, whiles, doors, name, engine):
        self.whiles = whiles
        self.doors = doors
        self.name = name
        self.engine = engine

    def set_whiles(self, whiles):
        self.whiles = whiles

    def set_door(self, doors):
        self.doors = doors

    def set_name(self, name):
        self.name = name

    def set_engine(self, engine):
        self.engine = engine

    def get_whiles(self):
        return self.whiles

    def get_doors(self):
        return self.doors

    def get_name(self):
        return self.name

    def get_engine(self):
        return self.engine

    def display_info(self):
        print (" Car brand:", self.get_name(), "\tNumber of doors:",
               self.get_doors(), "\n", "Number of Whiles:", self.get_whiles(),
               "\tType engine:", self.get_engine(), "\n")

class Truck(Automobile):
    pass


class Car(Automobile):
    pass

BMW = Car(4, 3, "BMW", "V8")
BMW.display_info()

BMW = Truck(6, 2, "КАМАЗ", "Daimler OM 457LA")
BMW.display_info()