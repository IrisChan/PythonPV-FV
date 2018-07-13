from decimal import *
import pandas as pandas
import numpy as np

def pv(fv, rate, nPeriods):
    """
    Compute the present value.

    Given:
        * `fv`: future value
        * `rate`: interest rate
        * `nPeriods`: number of periods

    Return: 
        Present value with output round to two decimal places with valid inputs. If number of periods is 
        smaller than 0, return valueError
    """
    if nPeriods < 0:
        raise ValueError("Number of periods should be non-negative.")

    temp = (1+rate)**nPeriods
    pv = Decimal(fv / temp)
    res = Decimal(pv.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))

    return res

def printPV(fv, rate, nPeriods):
    # Print out the present value given future value, rate, and number of periods.

    try:
        val = pv(fv, rate, nPeriods)
        print(('With future value = {0}, rate = {1}, number of '
              'periods = {2}, the present value is {3}.').format(fv, rate, nPeriods, val))
    except ValueError as e:
        print(e)

def getPVs(filePath):
    '''
    Read future value, rate, number of periods from a .csv file, compute the present value for each of them

    Given:
        `filePath': the absolute path for the .csv file

    Return:
        `df`: dataframe that contains pv, fv, rate, nPeriods.
    '''
    try:
        df = pandas.read_csv(filePath, converters={'fv': Decimal, 'rate': Decimal, 'nPeriods': Decimal})
        
        # Apply the pv function to each row read from .csv file and create an additional column 'pv' to keep the result.
        df['pv'] = df.apply(lambda row: pv(row['fv'], row['rate'], row['nPeriods']), axis = 1)

        print(df)
    except Exception, e:
        print("Error in reading " + filePath)
        print e
        df = pandas.DataFrame()
    
    return df


if __name__ == '__main__':
    # Problem 4
    printPV(1000, 0.1, 5)

    # Problem 5
    getPVs('inputToProblem5.csv')
