from multipledispatch import dispatch


class PolymorphismExample:
    @dispatch(int, int)
    def get_sum(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def get_sum(self, a, b, c):
        return a + b + c


""" Creating object for PolymorphismExample Method overloading example"""

poly = PolymorphismExample()
print(f"Sum of 10 + 20: {poly.get_sum(10, 20)}")
print(f"Sum of 10 + 20 + 30: {poly.get_sum(10, 20, 30)}")
