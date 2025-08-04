class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be positive")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Exceded the capacity of jar")
        else:
            self._size = self._size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Not enough cookies in the jar")
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(4)
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()
