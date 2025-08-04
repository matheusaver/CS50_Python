import pytest
from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar(4)
    assert jar.capacity == 4
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(8)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)


if __name__ == "__main__":
    main()
