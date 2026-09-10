# Custom iterator example

class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


numbers = CountUp(3)

for number in numbers:
    print(number)