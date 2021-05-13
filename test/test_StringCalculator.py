import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from stringCalculator import StringCalculator
import pytest

@pytest.fixture
def strCal():
    stringCalculator = StringCalculator()
    return stringCalculator

def test_add_empty_string(strCal):
    assert strCal.add("") == 0

def test_add_simple_string_only_one_digit(strCal):
    result = strCal.add("1")
    assert result == 1

def test_add_simple_string_only_multi_digit(strCal):
    result = strCal.add("100")
    assert result == 100

def test_string_with_comma(strCal):
    assert strCal.add("1,2") == 3

def test_string_with_multiple_numbers(strCal):
    assert strCal.add("1,1,1,1,1") == 5

def test_string_with_newline_between(strCal):
    assert strCal.add("1\n2,3") == 6

def test_string_with_delimiters(strCal):
    assert strCal.add("//;\n1;2") == 3

def test_string_with_one_negative(strCal):
    with pytest.raises(ValueError):
        strCal.add("-1") 

def test_string_with_mutiple_negative(strCal):
    with pytest.raises(ValueError):
        strCal.add("-1,-1,-1") 

def test_number_greater_1000(strCal):
    assert strCal.add("2,1001") == 2

def test_string_with_diff_delimiters(strCal):
    assert strCal.add("//[***]\n1***2***3") == 6

def test_string_with_multiple_delimiters(strCal):
    assert strCal.add("//[*][%]\n1*2%3") == 6

def test_string_with_multiple_delimiters_longer_than_1(strCal):
    assert strCal.add("//[**][%$]\n1**2%$3") == 6