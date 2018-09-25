""" Newton's Method Functions"""
#Lauren Giurini
import numpy as np


def newton(f, df, guess, tolerance, ITmax):
    y = guess
    count = 1
    E= tolerance + 1
    y1 = guess
    while E > tolerance and count < ITmax:
        y1 = y - f(y)/df(y)
        E = np.abs(y - y1)
        y = y1
        count = count + 1
    return y1, count
