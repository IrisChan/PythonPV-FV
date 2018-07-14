from decimal import *
import pandas as pandas
import numpy as np

DOLLAR_QUANTIZE = Decimal('0.01')

def dollar(amount, round=ROUND_CEILING):
    '''
    Return amount to `DOLLAR_QUANTIZE` decimal places.
    '''
    if not isinstance(amount, Decimal):
        amount = Decimal(str(amount))
    
    return amount.quantize(DOLLAR_QUANTIZE, rounding = round)

class Calculations:
    def readFromFile(self, filePath):
        # Read a dataframe from .csv file specified in `filePath`

        try:
            df = pandas.read_csv(filePath, converters={'fv': Decimal, 'rate': Decimal, 'nPeriods': Decimal})
            return df
        except Exception, e:
            raise Exception("Error in reading " + filePath)        
 
    def computePV(self, fv, rate, nPeriods):
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
        try:
            model = FModel(fv, rate, nPeriods)
            pv = model.pv()
               
            return pv
        except ValueError as e:
            print(e)

    def computePVfromFile(self, filePath):
        '''
        Read future value, rate, number of periods from a .csv file, compute the present value for each of them

        Given:
            `filePath`: the absolute path for the .csv file

        Return:
            `df`: dataframe that contains pv, fv, rate, nPeriods.
        '''
        try:
            df = self.readFromFile(filePath)

            # Apply the pv function to each row read from .csv file and create an additional column 'pv' to keep the result.
            df['pv'] = df.apply(lambda row: self.computePV(row['fv'], row['rate'], row['nPeriods']), axis = 1)
        except Exception, e:
            print(e)
            df = pandas.DataFrame()
        
        return df       

    def computeDelta(self, fv1, r1, nPeriods1, fv2, r2, nPeriods2):
        '''
        Compute the `delta of pv / delta of rate`

        Given:
            `fv1`, `r1`, `nPeriods1`: the first future value, rate, number of periods
            `fv2`, `r2`, `nPeriods2`: the second future value, rate, number of periods

        Return:
            `delta`: delta of pv / delta of rate
        '''
        if (r1 == r2):
            return np.nan
        
        fm1 = FModel(fv1, r1, nPeriods1)
        fm2 = FModel(fv2, r2, nPeriods2)

        delta = dollar((fm1.pv() - fm2.pv()) / (fm1.rate() - fm2.rate()))
        return delta

    def computeDeltaFromFile(self, filePath):
        df = self.readFromFile(filePath)

        for i in range(1, len(df)):
            if (i == 0):
                df.loc[i, 'delta'] = np.nan
            else:
                df.loc[i, 'delta'] = self.computeDelta(df.loc[i - 1, 'fv'], df.loc[i - 1, 'rate'], df.loc[i - 1, 'nPeriods'], df.loc[i, 'fv'], df.loc[i, 'rate'], df.loc[i, 'nPeriods'])

        return df       

    def print_summary(self, fv, rate, nPeriods, pv):
        print(('With future value = {0}, rate = {1}, number of '
               'periods = {2}, the present value is {3}.\n').format(fv, rate, nPeriods, pv))
 

class FModel:
    def __init__(self, fv, rate, nPeriods):
        if nPeriods < 0:
            raise ValueError("Number of periods should be non-negative.\n")

        self._fv = fv
        self._rate = rate
        self._nPeriods = nPeriods
        self._pv = np.nan

    def pv(self):
        if np.isnan(self._pv):
            temp = (1 + self.rate()) ** self.nPeriods()
            self._pv = dollar(self.fv() / temp)
        
        return self._pv

    def fv(self):
        return self._fv

    def rate(self):
        return self._rate

    def nPeriods(self):
        return self._nPeriods


def main():
    # Problem 4
    print("Output to problem 4:")
    cal = Calculations()
    pv = cal.computePV(1000, 0.1, 5)
    cal.print_summary(1000, 0.1, 5, pv)

    # Problem 5
    print("Output to problem 5:")
    df = cal.computePVfromFile('inputToProblem5.csv')
    print(df)
    print('\n')

     # Problem 8
    print("Output to problem 8:")
    df = cal.computeDeltaFromFile('inputToProblem8.csv')
    print(df) 


if __name__ == '__main__':
    main()

    
'''
With future value = 1000, rate = 0.1, number of periods = 5, the present value is 620.93.

Output to problem 5:
       fv  rate nPeriods      pv
0  100.00  0.05        1   95.24
1  -50.00  0.05        2  -45.35
2   35.00  0.05        3   30.24
3  -35.00  0.05        1  -33.33
4   50.00  0.05        1   47.62


Output to problem 8:
        fv  rate nPeriods     delta
0   500.00  0.07        1       NaN
1   750.00  0.10        3   3206.67
2  -550.00  0.03        2  15455.86
'''