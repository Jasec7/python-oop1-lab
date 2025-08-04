#!/usr/bin/env python3
# Define a Coffee class that models a coffee with a size and a price
class Coffee:
# Initialize a new Coffee instance with size and price
    def __init__(self,size, price):
        self.size = size
        self.price = price

# Property getter for size
    @property
    def size(self):
        return self._size
    
# Property setter for size with validation
    @size.setter
    def size(self, size):
        # Ensure size is one of the accepted values
        if size in ["Small","Medium","Large"]:
             self._size = size

        else:
            print("size must be Small, Medium, or Large")

 # Property getter for price
    @property
    def price(self):
        return self._price
    
# Property setter for price with validation
    @price.setter
    def price(self, price):
        # Ensure price is a number (int or float)
        if isinstance(price, (float, int)):
             self._price = price

        else:
            print("missing money")
# Method that simulates giving a tip by increasing the price
    def tip(self):
        print('This coffee is great, here’s a tip!')
        self._price += 1
