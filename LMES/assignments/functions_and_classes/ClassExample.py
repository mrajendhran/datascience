class SmartPhoneClassExample:
    # Constructor method called during every object creation (Magic method)
    def __init__(self, model, released_year, brand):
        self.model = model
        self.released_year = released_year
        self.brand = brand


""" Creating a iphone object from SmartPhone class"""

iphone = SmartPhoneClassExample(11, 2022, "iPone")
print("printing iphone object attributes:")
print(iphone.model)
print(iphone.released_year)
print(iphone.brand)
