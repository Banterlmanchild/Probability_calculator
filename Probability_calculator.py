#! /usr/bin/env python2.7

__author__ = "Adam Richardson"
__date__ = '08/02/17'


class Factorial:
    def __init__(self, n):
        self.n = n
        if self.n < 0.0:
            raise ValueError("Cannot have a negative factorial")
        elif self.n != int(self.n):
            raise ValueError("Cannot have non-integer factorial")

    def factorial(self):
        if self.n == 0.0:
            return 1.0
        else:
            return self.n * Factorial(self.n - 1.0)
g