"""A collection of Data Science helper functions"""

import pandas as pd 
import numpy as np 
import random

def df_cleaner(df):
    """Clean a df of nulls"""
    return df.dropna()


"""Check to make sure that code works"""
print("df_cleaner is working!") 


def null_count(df):
    """Check a dataframe for nulls and return the 
    number of missing values"""
    return df.isnull().sum().sum()


"""Check to make sure that code works"""
print("null_count is working!")


def train_test_split(df, frac):
    """
    Create a Train/Test split function for a dataframe and return both 
    the Training and Testing sets.
    Frac refers to the percent of data you would like to set aside
    for training.
    """
    frac = round(len(df)*frac)
    train = df[:frac]
    test = df[frac:]

    return train, test


"""Check to make sure that code works"""
print("train_test_split is working!")


def randomize(df, seed):
    """
    Testing randomize(df) function: Develop a 
    randomization function that randomizes all of 
    a dataframes cells then returns that randomized dataframe
    """
    """NOTE: I am not sure about the seed part."""
    #seed = np.random.seed(0)
    """Randomly sample 100% of your df"""
    df = df.sample(frac=1, random_state=seed)#.reset_index(drop=True)
    return df


"""Check to make sure that code works"""
print("randomize is working!")

    
def addy_split(add_series):
    cities = []
    states = []
    zipcodes = []
    for row in add_series.iterrows():
        alist = row.split()
        #if statements to find city
        city = [word for word in alist if word[-1] == ',']
        cities.append(city)
        #if statements to find state
        state = [piece for piece in alist if len(piece) == 2 and piece[:2].isupper() == True]
        states.append(state)
        # if statements to zipcode
        zipcode = [n for n in alist if len(n) == 5 and n.isdigit() == True]
        zipcodes.append(zipcode)
        df = pd.DataFrame({'city': cities, 'state': states, 'zip': zipcodes})
    return df



"""Check to make sure that code works"""
print("addy_split is working!")


def abbr_2_st(state_series, abbr_2_st=True):
    """
    Return a new column with the full name from a State
    abbreviation column -> An input of FL would return Florida.
    This function should also take a boolean (abbr_2_state)
    and when False takes full state names and return state abbreviations.
    -> An input of Florida would return Fl.
    """
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
    if abbr_2_st == True:
      inv_map = {v: k for k, v in us_state_abbrev.items()}
      full_names = []
      for abbv in state_series:
        full_names.append(inv_map[abbv])
      return full_names
    else:
      # Return Abbreviation
      abbvs = []
      for full_name in state_series:
        abbvs.append(us_state_abbrev[full_name])
      return abbvs



FAVORITE_ANIMALS = ['dolphin', 'whale', 'seadragon', 'wolf', 'tiger']
FAVORITE_COLORS = ['pink', 'blue', 'purple', 'green']

def add(x1, x2):
    return x1 + x2
    

def increment(x):
    return x + 1

"""Check to make sure code works all the way through"""
print("it worked!")