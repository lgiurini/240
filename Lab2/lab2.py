"""Lab 2 Rootfinding """
#Lauren Giurini
#lab 2 call file
#souris, lievre
import matplotlib.pyplot as plt
import numpy as np
# from bisection import *
from newton import *

# #excercise 2 #########################
# #x = symbol('x')
# def f(x):
#   return (x**6)-x-1.0
# #bisection(f, 1, 2, 5E-4, 12)
# c, count = bisection2(f, 1, 2, 5E-4, 20)
# print( "zero at:", c)
# print("iterations:", count)
#
# #excercise 3 ######################
# def f(x):
#     return (32*x**6) - (48*x**4) + (18*x**2) - 1
# # plot roots
# plot_roots(f, -3, 3, 150, -2, 10)
#
# c, count = bisection2(f, -1.5, -0.8, 10E-10, 20)
# print( "1. zero at:", c)
#
# c, count = bisection2(f, -0.8, -0.5, 10E-10, 20)
# print( "2. zero at:", c)
#
# c, count = bisection2(f, -0.5, 0.0, 10E-10, 20)
# print( "3. zero at:", c)
#
# c, count = bisection2(f, 0.0, 0.5, 10E-10, 20)
# print( "4. zero at:", c)
#
# c, count = bisection2(f, 0.5, 0.8, 10E-10, 20)
# print( "5. zero at:", c)
#
# c, count = bisection2(f, 0.8, 1.2, 10E-10, 20)
# print( "6. zero at:", c)
#
#
# #print("total is {0:.5E} ir {1:3d}. format (a, c))
#
# #excercise 4 ########################
# def f(x):
#      return np.exp(x) - x - 2
#
# plot_roots(f, -2.5, 2.5, 150, -7.5, 10)
#
# c, count = bisection2(f, -2.0, -1.0, 5E-8, 20)
# print( "zero at:", c)
# print( "iterations:", count)
#
# c, count = bisection2(f, 1.0, 2.0, 5E-8, 20)
# print( "zero at:", c)
# print( "iterations:", count)

#####################################
def f(x):
    return x**6

def df(x):
    return 6*x**5

print(newton(f, df, 10.0, 1E-16, 5000))
