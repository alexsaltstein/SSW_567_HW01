# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr

Last Updated on Mon Feb 8 2021

Implemented methods and added testing functions

@author: Alex Saltstein
"""

import unittest     # this makes Python unittest module available


def classifyTriangle(a, b, c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If the sum of any two sides equals the square of the third side, then return 'Right'
        If no pair of  sides are equal, return 'Scalene'
        else not a valid triangle, then return 'NotATriangle'
    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if a == b and a == c and b == c:
        return 'Equilateral'
    elif (a == b and b != c) or (a == c and b != c) or (b == c and b != a):
        return 'Isoceles'
    elif ((a + b) == (c*c) or (a + c) == (b*b) or (b+c) == (a*a)):
        return 'Right'
    elif (a != b and b != c and a != c):
        return 'Scalene'
    else:
        return 'NotATriangle'


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=',
          classifyTriangle(a, b, c), sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testMyTestSet2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10, 10, 10),
                            'Isoceles', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(10, 15, 30),
                         'Scalene', 'Should be Isoceles')


if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1, 2, 3)
    runClassifyTriangle(1, 1, 1)

    # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=False)
    # unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
