"""Practicing OOP"""
import pandas as pd 
import numpy as np 


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name} is {self.age} years old"


    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


if __name__ == "__main__":

    miles = Dog("Miles", 4)
    print(miles)


