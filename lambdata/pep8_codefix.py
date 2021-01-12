"""Code to be fixed using Pep8 style Guide"""


"""In style_example.py file"""


"""what would you say if you were working with 
   someone and this is the code they gave you?
"""


import math, sys 


def example_1():
    """THIS IS A LONG COMMENT AND should be wrapped 
    to fit within a 72 character limit
    """
    some_tuple = (1, 2, 3, 'a')
    some_variable = {"long":
        'LONG CODE LINES should be wrapped within 79 character to prevent page cutoff stuff',
                 "other":
                 [math.pi, 
                 100,
                 200, 
                 300, 
                 9999292929292, 
                 'This IS a long string that looks gross and goes beyond what it should']}
    more = {"inner": "THIS whole logical line should be wrapped", 
            "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]}

    return (some_tuple, some_variable, more)


def example_2(): 
    return {"has_key() is deprecated": True}


class Example3(object):
    def __init__(self, bar):
        self.bar = bar 
    
    
    def bar_string(self):
        some_string = ("INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented",
    "THIS IS MORE CODE")
        if {"bar": self.bar * self.bar}:
            return self.bar
        else:
            return (self, some_string)



    