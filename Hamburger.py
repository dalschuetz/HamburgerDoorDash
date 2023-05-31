# Group 5
# Dallen Schuetzler, Naomy Sanchez, James Goaslind, Koyun Li, Yuto Takamura, Allan Foote
# Door Dash Hamburgers Group Project

# import random for later functions
import random

# creating the order class and adding the random burger count function
class Order():
    def __init__(self) -> None:
        self.burgercount = Order.randomBurgers(self)
    
    def randomBurgers(self):
        burger_count = random.randint(1,20)
        return burger_count

# creating the person class which has the random name generation function
class Person():
    def __init__(self) -> None:
        self.customer_name = Person.randomName(self)
    
    def randomName(self):
        asCustomer = random.choice(["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"])
        return asCustomer

# creating the customer subclass which will run the full process
class Customer(Person):
    def __init__(self, order) -> None:
        super().__init__()
        self.order = order
        # dictionary of names attached to the number of burgers in their order
        self.dictionary = {
            'Jefe' : 0,
            'El Guapo' : 0,
            'Lucky Day': 0,
            'Ned Nederlander': 0,
            'Dusty Bottoms': 0,
            'Harry Flugleman': 0,
            'Carmen': 0,
            'Invisible Swordsman': 0,
            'Singing Bush': 0
        }
        # appends dictionary to later add burgers to the names
    def append_dictionary(self,key,value):
        self.dictionary[key] += value

    # the total run function which will run the loop the same amount of times as people in the queue
    # the loop picks a random name, adds a random number to the name in the dictionary, makes the dictionary into a list
    def run(self, icustomer):
        self.queue = icustomer
        for x in range (self.queue):
            self.name = Person.randomName(self) 
            self.order = Order.randomBurgers(self)
            self.append_dictionary(self.name, self.order)
            self.list()
        # prints list
        self.printlist()
        # pops the list to clear the queue
        for x in self.listSortedCustomers:
            self.listSortedCustomers.pop(0)
    
    # makes a list out of the dictionary
    def list(self):
        self.listSortedCustomers = sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)
    
    # prints the list we just made
    def printlist(self):
        for x in self.listSortedCustomers:
            print(x[0].ljust(19),"\t", x[1])

# instance of the customer to run the code, asks for number of customers in the queue
a1 = Customer(10)
a1.run(int(input('Number of Customers : ')))