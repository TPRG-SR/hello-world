'''
TPRG 2131 Fall 202x Assignment 1, Test file template.
Sept, 202x
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

# test_A_V_calc.py
"""
Unit Tests for A/V Calculator Module
This file contains tests for the functions in A_V_calc.py using pytest.
"""

# test_A_V_calc.py

import pytest
from A_V_calc_starter2 import A_V_CALC


def test_rectangle_area():
    calculator = A_V_CALC()
    assert calculator.rectangle_area(5, 3) == 15
    assert calculator.rectangle_area(0, 10) == 0
    assert calculator.rectangle_area(-5, 5) == -25

def test_circle_area():
    calculator = A_V_CALC()
    assert round(calculator.circle_area(1), 2) == round(3.14, 2)
    assert round(calculator.circle_area(0), 2) == 0
    assert round(calculator.circle_area(2.5), 2) == round(19.63, 2)

def test_sphere_volume():
    calculator = A_V_CALC()
    assert round(calculator.sphere_volume(1), 2) == round(4.19, 2)
    assert round(calculator.sphere_volume(0), 2) == 0
    assert round(calculator.sphere_volume(3), 2) == round(113.10, 2)

def test_cylinder_volume():
    calculator = A_V_CALC()
    assert round(calculator.cylinder_volume(1, 2), 2) == round(6.28, 2)
    assert round(calculator.cylinder_volume(0, 5), 2) == 0
    assert round(calculator.cylinder_volume(2, 5), 2) == round(62.83, 2)

def test_cube_volume():
    calculator = A_V_CALC()
    assert calculator.cube_volume(1) == 1
    assert calculator.cube_volume(0) == 0
    assert calculator.cube_volume(3) == 27
