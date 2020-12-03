"""Lambdata - a collection of Data Science helper functions"""

import pandas as pd 
import numpy as np 


def df_cleaner(df):
    """Clean a df of nulls"""
    # TODO - implement
    return df.dropna()


"""Check to make sure that code works"""
print("it half way worked") 


def null_count(df):
    """Returns the sum of missing values"""
    return df.isnull().sum()


FAVORITE_ANIMALS = [['dolphin', 'whale', 'seadragon', 'wolf', 'tiger']]


"""Check to make sure code works all the way through"""
print("it worked!")