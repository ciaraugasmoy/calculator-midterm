'''
Tests for calculation and divide 0
'''
from decimal import Decimal
import pytest
from app.calculator import Calculator,add,subtract,divide,multiply

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4
