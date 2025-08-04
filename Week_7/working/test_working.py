from working import convert
import pytest

def main():
    test1()
    test2()

def test1():
    assert convert("5 AM to 2 PM") == "05:00 to 14:00"
    assert convert("5 AM to 2:00 PM") == "05:00 to 14:00"
    assert convert("5:00 AM to 2 PM") == "05:00 to 14:00"
    assert convert("7:00 AM to 3:00 PM") == "07:00 to 15:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("11:15 PM to 6:30 AM") == "23:15 to 06:30"

def test2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
