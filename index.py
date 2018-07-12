from decimal import *

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

if __name__ == '__main__':
    printPV(1000, 0.1, 5)
