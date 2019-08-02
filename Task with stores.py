class Store:
    total_amount = 0

    def __init__(self, name, profit):
        self.name = name
        self.profit = profit

    def set_name(self, name):
        self.name = name

    def set_profit(self, profit):
        self.profit = profit

    def get_name(self):
        return self.name

    def get_profit(self):
        return self.profit

    def display_info (self):
        print ("Name store:", self.get_name(), "\tProfit store:", self.get_profit())

    def __add__(self, other):
        return (self.get_profit() + other.get_profit())

    def __repr__(self):
        return '{}, {}'.format(self.get_name(), self.get_profit())

Vishnya = Store('Vishnya', 25)
Vishnya.display_info()

Troc = Store('Troc', 53)
Troc.display_info()

print("The total profit of stores: ", Vishnya + Troc)