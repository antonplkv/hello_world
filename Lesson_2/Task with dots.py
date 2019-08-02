# class Test:
#
#     def __eq__(self, other):                        #__eq__ для сравнения
#         result = self.__class__ == other.__class__
#         return result
#
#     def __neg__(self):                              # __neg__ унарный минус
#         result = self.get_seats() * -1
#         return result
#
class Point:

    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_x (self, x):
        self.x = x

    def set_y (self, y):
        self.y = y

    def set_z (self, z):
        self.z = z

    def get_x (self):
        return self.x

    def get_y (self):
        return self.y

    def get_z (self):
        return self.z

    def __add__ (self, other):
        return Point(self.get_x () + other.get_x (), self.get_y () + other.get_y (), self.get_z () + other.get_z ())

    def __sub__ (self, other):
        return Point(self.get_x () - other.get_x (), self.get_y () - other.get_y (), self.get_z () - other.get_z ())

    def __mul__ (self, other):
        return Point(self.get_x () * other.get_x (), self.get_y () * other.get_y (), self.get_z () * other.get_z ())

    def __truediv__ (self, other):
        return Point(self.get_x () / other.get_x (), self.get_y () / other.get_y (), self.get_z () / other.get_z ())

    def __repr__(self):
        return '{}, {}, {}'.format(self.get_x(), self.get_y(), self.get_z())

add = Point (1, 2, 3)
add2 = Point (1, 2, 3)

print ("Point + Point:\t", add + add2)
print ("Point - Point:\t", add - add2)
print ("Point * Point:\t", add * add2)
print ("Point / Point:\t", add / add2)
