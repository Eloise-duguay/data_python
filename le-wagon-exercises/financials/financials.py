# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
import math
from math import *

def forward_price(spot, interest_rate, time):
    forward_price = spot*(e**(interest_rate*time))
    forward_price = round(forward_price,2)
    return forward_price

# TODO: 2nd exercise: Define the `short_pnl` function
    
def short_pnl(positions, mtm):
    nbr_positions = len(positions)
    nbr_mtm = len(mtm)
    if nbr_positions != nbr_mtm:
        print('error')
    else:
        result = 0
        for i in range(0,nbr_mtm):
            result += positions[i] - mtm[i]
        return result

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

spot = 1.18
interest_rate = 2.18
time = 3.18

forward_price = forward_price(spot, interest_rate, time)
print(forward_price)

positions= [ 100, 140, 200 ]
mtm= [ 110, 120, 180 ]
short_pnl(positions, mtm)

for index, value in enumerate(mtm):
    print(index, value)
