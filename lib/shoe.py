#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9):
        self.brand = brand
        self.size = size
        self._condition = "New"

    @property
    def size(self):
        """The size property"""
        return self._size

    @size.setter
    def size(self, size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        """Repairs the shoe and sets the condition to 'New'."""
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def condition(self):
        """The condition property"""
        return self._condition

    @condition.setter
    def condition(self, condition):
        self._condition = condition