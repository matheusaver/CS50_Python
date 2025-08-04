import pytest
from seasons import convert


def main():
    test()


def test():
    assert convert("2024-07-08") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2023-07-08") == "One million, fifty-two thousand, six hundred forty minutes"
    with pytest.raises(SystemExit):
        convert("September 20th, 1835")


if __name__ == "__main__":
    main()
