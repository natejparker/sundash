"""
File: sunspotcycle.py
Description: Functions that process the dataframe for sunspot cycles
Author: Nathan Parker
Date: 15 October 2023
"""
def cycle_modulo(year, cycle):
    """ Takes a year and given a sunspot cycle length, determines how many years into the cycle that year was

    Args:
        year (real): Year that the data was recorded
        cycle (real): Length of the sunspot cycle
    Return:
        cycle_position (real): Years into the sunspot cycle
    """
    cycle_position = year % cycle
    return cycle_position

# Using alter_series developed in hw1
def df_cycle(df, attribute, cycle):
    """ Iterates over a series in a dataframe and performs cycle modulo

        Args:
            df (pandas.DataFrame): dataframe that wants to be altered
            attribute (string): column name to be altered in the dataframe
            cycle (real): Length of the sunspot cycle
        """
    for i in range(len(df)):
        df.loc[i, attribute] = cycle_modulo(float(df.loc[i, attribute]), cycle)