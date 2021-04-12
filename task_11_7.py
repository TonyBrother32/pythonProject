class ComplexDigit:
    def __init__(self, digit):
        self.digit = digit

    def __add__(self, other):
        return self.digit + other.digit

    def __mul__(self, other):
        return self.digit * other.digit


complex_1 = ComplexDigit(3 + 5j)
complex_2 = ComplexDigit(1 - 7j)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
