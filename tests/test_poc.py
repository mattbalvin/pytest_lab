from libpoc.poc import *

def test_number_ten():
  assert number_ten() == 10

def test_simple_function():
  assert "simple_function" in simple_function("foo")
