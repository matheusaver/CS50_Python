import pytest
from numb3rs import validate

def main():
    test_correct()
    test_incorrect()
    test_text()
    test_format()
    test_number()
    test_special_case()

def test_correct():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
def test_incorrect():
    assert validate("256.256.256.256") == False
    assert validate("0.0.0.0") == True
def test_text():
    assert validate("matheus") == False
    assert validate("ABC.ABC.ABC.ABC") == False
def test_format():
    assert validate("123.123.123.123.123") == False
    assert validate("123.123.123.1234") == False
    assert validate("123.123.123") == False
    assert validate("123/123/123/123") == False
def test_number():
    assert validate("123.123.123.123") == True
    assert validate("350.1.1.1") == False
    assert validate("1.350.1.1") == False
    assert validate("1.1.350.1") == False
    assert validate("1.1.1.350") == False
def test_special_case():
    assert validate("127.0.0.1") == True


if __name__ == "__main__":
    main()
