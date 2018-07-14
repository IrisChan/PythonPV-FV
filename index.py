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
        raise ValueError("Number of periods should be non-negative.\n")

    temp = (1+rate)**nPeriods
    pv = Decimal(fv / temp)
    res = Decimal(pv.quantize(Decimal('.01'), rounding=ROUND_CEILING))

    return res

def printPV(fv, rate, nPeriods):
    # Print out the present value given future value, rate, and number of periods.

    try:
        val = pv(fv, rate, nPeriods)
        print(('With future value = {0}, rate = {1}, number of '
              'periods = {2}, the present value is {3}.\n').format(fv, rate, nPeriods, val))
    except ValueError as e:
        print(e)

def getPVs(filePath):
    '''
    Read future value, rate, number of periods from a .csv file, compute the present value for each of them

    Given:
        `filePath`: the absolute path for the .csv file

    Return:
        `df`: dataframe that contains pv, fv, rate, nPeriods.
    '''
    try:
        df = pandas.read_csv(filePath, converters={'fv': Decimal, 'rate': Decimal, 'nPeriods': Decimal})
        
        # Apply the pv function to each row read from .csv file and create an additional column 'pv' to keep the result.
        df['pv'] = df.apply(lambda row: pv(row['fv'], row['rate'], row['nPeriods']), axis = 1)
    except Exception, e:
        print("Error in reading " + filePath)
        print(e)
        df = pandas.DataFrame()
    
    return df


def delta(pv1, pv2, rate1, rate2):
    '''
    Compute the `delta of pv / delta of rate`

    Given:
        `pv1`: the first present value
        `pv2`: the second present value
        `rate1`: the first rate
        `rate2`: the second rate

    Return:
        `delta`: delta of pv / delta of rate
    '''
    if (rate1 == rate2):
        return np.nan
    
    delta = (pv1 - pv2) / (rate1 - rate2)

    res = Decimal(delta.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))

    return res

def getDeltas(filePath):
    '''
    Read future value, rate, number of periods from a .csv file, compute the `delta of pv / delta of rate` for each of them

    Given:
        `filePath': the absolute path for the .csv file

    Return:
        `df`: dataframe that contains pv, delta, fv, rate, nPeriods.
    '''
    df = getPVs(filePath)

    for i in range(1, len(df)):
        if (i == 0):
            df.loc[i, 'delta'] = np.nan
        else:
            df.loc[i, 'delta'] = delta(df.loc[i - 1, 'pv'], df.loc[i, 'pv'], df.loc[i - 1, 'rate'], df.loc[i, 'rate'])

    return df

if __name__ == '__main__':
    # Problem 4
    print("Output to problem 4:")
    printPV(1000, 0.1, 5)

    # Problem 5
    print("Output to problem 5:")
    df = getPVs('inputToProblem5.csv')
    print(df)
    print('\n')

    # Problem 8
    print("Output to problem 8:")
    df = getDeltas('inputToProblem8.csv')
    print(df)
    print('\n')



'''
Output to problem 4:
With future value = 1000, rate = 0.1, number of periods = 5, the present value is 620.93.

Output to problem 5:
       fv  rate nPeriods      pv
0  100.00  0.05        1   95.24
1  -50.00  0.05        2  -45.35
2   35.00  0.05        3   30.24
3  -35.00  0.05        1  -33.33
4   50.00  0.05        1   47.62


Output to problem 8:
        fv  rate nPeriods       pv     delta
0   500.00  0.07        1   467.29       NaN
1   750.00  0.10        3   563.49   3206.67
2  -550.00  0.03        2  -518.42  15455.86


'''