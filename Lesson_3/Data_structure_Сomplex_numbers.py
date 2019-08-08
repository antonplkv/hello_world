# Стек:
class Stack():

    listok = []

    def append(self, item):
        self.listok.append(item)

    def pop(self, item):
        if item == 0:
            return self.listok.pop(item)
        else:
            print ("The stack works on the system 'LIFO'!")

    def rev(self):
        return self.listok.reverse()

    def result(self):
        return self.listok

x = Stack()
x.append("saf")
x.append(44)
x.append("kuki")
x.rev()
print("This is your list:",x.result())
x.pop(0)
print("This is your list after deletion:",x.result())

# Очередь:
class Turn():

    listok = []

    def append(self, item):
        self.listok.append(item)

    def pop(self, item):
        if item == -1:
            return self.listok.pop(item)
        else:
            print ("The queue is running on the system 'FIFO'!")

    def rev(self):
        return self.listok.reverse()

    def result(self):
        return self.listok

x = Turn()
x.append("saf")
x.append(44)
x.append("kuki")
x.rev()
print(f"This is your list: {x.result()}")
x.pop(-1)
print(f"This is your list after deletion: {x.result()}")

# Комплексные числа:

class ComplexNumbers:

    z1 = complex(2, 5)
    z2 = complex(4, 2)

    def get_num_z1(self):
        return self.z1

    def get_num_z2(self):
        return self.z2

    def __add__(self, other):
        return ComplexNumbers (self.get_num_z1() + other.get_num_z2())

    def __sub__(self, other):
        return ComplexNumbers (self.get_num_z1() - other.get_num_z2())

    def __mul__(self, other):
        return ComplexNumbers (self.get_num_z1() * other.get_num_z2())

    def __truediv__(self, other):
        return ComplexNumbers (self.get_num_z1() / other.get_num_z2())



Z1 = ComplexNumbers.z1
Z2 = ComplexNumbers.z2

print("The addition of complex numbers:",Z1 + Z2)
print("The subtraction of complex numbers:",Z1 - Z2)
print("The multiplication of complex numbers:",Z1 * Z2)
print("The division of complex numbers:",Z1 / Z2)