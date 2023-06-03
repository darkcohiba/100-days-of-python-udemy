# *args
def addition(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(sum)


# addition(3, 3, 3, 3, 3, 1)


# **kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, add=8, multiply=5)

# kwargs in a class

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

