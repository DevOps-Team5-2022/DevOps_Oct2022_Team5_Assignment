import pytest
from helloworld import *

def test_successString():
  result1 = helloworld("item")
  assert result1 == "Hello item! Welcome to Hello World File!"

def test_longString():
  result2 = helloworld("Stringtoolong")
  assert result2 == "Input string too long!"

def test_emptyString():
  result3 = helloworld("")
  assert result3 == "Input string is empty!"
