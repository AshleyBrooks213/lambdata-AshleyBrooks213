"""A collection of helper functions for Acme Corporation"""
import random
import unittest


class Product:
    def __init__(
        self,
        name,
        price=10,
        weight=20, 
        flammability=0.5, 
        identifier=random.randint(1000000, 999999, 1)):
        """Constructor for Product class"""
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)


    

