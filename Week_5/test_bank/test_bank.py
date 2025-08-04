from bank import value

def test_hello():
    assert value("hello") == 0
def test_hi():
    assert value("hi") == 20
def test_other():
    assert value("CS50") == 100
    assert value("abc123") == 100
def test_upper():
    assert value("HELLO") == 0
    assert value("Hi") == 20
