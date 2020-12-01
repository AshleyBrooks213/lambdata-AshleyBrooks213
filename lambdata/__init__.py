"""Lambdata - a collection of Data Science helper functions"""

import pandas as pd 
import numpy as np 

def df_cleaner(df):
    """Clean a df of nulls"""
    #TODO - implement
    df = df.dropna()

    return df 

def null_count(df):
    """Returns the sum of missing values"""
    return df.isnull().sum()



