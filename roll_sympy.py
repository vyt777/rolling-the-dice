# In order to find probability of rolling dice we can use formula for finding 
# number of compositions. Using sympy, which is close to math formulas, but 
# works slowly to compute coefficients of polynomial with big input numbers. 
# This solution has been rewritten using numpy.
# 1. Find the number of A-restricted compositions of n into exactly k parts 
# https://en.wikipedia.org/wiki/Composition_(combinatorics)#Number_of_compositions
# 2. Find the probability of getting exactly n number on a single roll of the given 
# k-sided dice ('A' is the number of dice)
# https://py.checkio.org/en/mission/probably-dice/

from sympy import summation, Poly
from sympy.abc import x, e

def roll(d_num, sides, target):
    """
    :param d_num: number of dices OR max size of each part of composition
    :param sides: sides of dice OR number of parts of composition
    :param target: number to get through rolling a single roll OR power in power 
    series
    :return: rounded probability
    """
    su = summation(x**e, (e, 1, sides)) ** d_num
    poly_coeffs = Poly(su, x).all_coeffs()[::-1]
    if target + 1 > len(poly_coeffs):
    	return 0
    num_of_compositions = poly_coeffs[target]
    probability = num_of_compositions / (sides**d_num)
    return (round(float(probability), 4)) 

assert roll(2, 6, 3) == 0.0556, "Basic example"
assert roll(2, 6, 4) == 0.0833, "More points"
assert roll(2, 6, 7) == 0.1667, "Maximum for two 6-sided dice"
assert roll(2, 3, 5) == 0.2222, "Small dice"
assert roll(2, 3, 7) == 0, "Never!"
assert roll(3, 6, 7) == 0.0694, "Three dice"
assert roll(10, 10, 50) == 0.0375, "Many dice, many sides"
# assert roll(10, 20, 1000) == 0, "Big numbers, never". # Slow calculations
