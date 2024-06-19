import pytest
import Calculator
from Calculator import *
from pytest import approx

# test adding two positive numbers:
def test_addition():
  result = add (4,5)
  assert result == 9

# test adding two negative numbers:
def test_addition():
  result = add (-1,-2)
  assert result == -3

# test adding a positive and a negative
def test_addition():
  result = add (-2,3)
  assert result == 1

# test subtracting two positive numbers:
def test_subtraction():
  assert subtract(5, 3) == 2

# test subtracting two negative numbers:
def test_subtraction():
  assert subtract(-4, -2) == -2

# test subtracting a larger number from a smaller one:
def test_subtraction():
  assert subtract(2, 5) == -3

# test multiplying two positive numbers:
def test_multiply():
  assert multiply(3, 4) == 12

# test multiplying two negative numbers:
def test_multiply():
  assert multiply(-3, -4) == 12

# test multiplying by zero:
def test_multiply():
  assert multiply(5, 0) == 0

# test division
# DONE: handles zero division
def test_divide():
  assert divide(4, 0) == "Cannot divide by 0"
  assert divide(10, 2) == 5
  assert divide(0,4) == 0

# test division by a negative number
def test_divide_negative():
  assert divide(20, -2) == -10
  assert divide(-20, -2) == 10
  assert divide(-20, 2) == -10

# test division by a floating-point number
def test_divide_float():
  assert divide(20, 6) == 20/6

# test when double 0 values entered
def test_doubleZeroInput():
    result = calculator.add(0, 0)
    assert result == 0

# test below doesn't run but wanted to consider testing wrong input
# need to change calculator code to handle wrong input first
def get_num(text):
  try:
     return int(input(f"\n{text}"))
  except ValueError:
     return "Please enter a valid integer"
