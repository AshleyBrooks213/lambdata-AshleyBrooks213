"""Lambdata - A collection of helper functions for Acme Corporation"""
import random
import unittest


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Constructor for Product class"""
        self.name = str(name)
        self.identifier = random.randint(1000000, 9999999)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        

    def stealability(self):
        """
        Calculates the price divided by the weight.
        Returns whether something is "Not so stealable...",
        "Kinda stealable...", or "Very stealable!"
        """
        ratio = self.price/self.weight 

        if ratio < 0.5:
            return "Not so stealable..."

        elif 0.5 <= ratio < 1.0:
            return "Kinda stealable..."

        else:
            return "Very stealable!"


    def explode(self):
        """
        Calculates the flammability times the weight.
        Returns: "...fizzle." if product is less than 10.
        Returns: "...boom!" if the product is equal to 10,
        but less than 50.
        Returns: "...BABOOM!!" otherwise.
        """
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."

        elif 10 == product < 50:
            return "...boom!"

        else: 
            return "...BABOOM!!"

    
class BoxingGlove(Product):
    """A subclass of Product"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        """A constructor for BoxingGlove that inherits from Product."""
        super().__init__(name, price, weight, flammability)
        

    
    def explode(self):
        """
        Overrides previous explode method and
        Always returns "...it's a glove."
        """
        return "...it's a glove."


    def punch(self):
        """
        Returns: "That tickles" if the weight is below 5.
        Returns: "Hey that hurt!" if the weight is great than 
        or equal to 5 but less than 15, and
        Returns: "OUCH!" otherwise.
        """
        if self.weight < 5:
            return "That tickles."

        elif 5 <= self.weight < 15:
            return "Hey that hurt!"

        else:
            return "OUCH!"


    


    

#if __name__ == "__main__":
   

