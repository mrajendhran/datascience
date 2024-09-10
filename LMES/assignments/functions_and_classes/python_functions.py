""" Simple basic greeting example to print string """


def greeting():
    print("Welcome home!")


greeting()

""" greeting method with parameter example """


def greeting(name):
    return f"Welcome {name}!"


message = greeting("Mohan")
print(message)

""" increment method with keyword argument example """


def increment(inputNumber, by):
    return inputNumber + by


sum = increment(3, by=5)
print(sum)

""" increment method with optional parameter with default value example """


def increment(inputNumber, by=1):
    return inputNumber + by


sum = increment(3)
print(sum)

""" multiply method with args example 
 *args means multiple params as tuple type """


def multiply(*args):
    total = 1
    for item in args:
        print(f"item => {item}")
        total *= item

    return total


result = multiply(3, 5, 6, 7, 8)
print(f"product of the list is: {result}")

""" saveUser method with args example 
 **args means multiple params as dictionary type """


def saveUser(**user):
    print(user["id"])
    print(user["firstName"])
    print(user["lastName"])
    print(user["skills"])


saveUser(id=1, firstName="Rajendran", lastName="Marimuthu", skills="Java, SpringBoot")




""" local and global variable scope example """



msg = "Hello World"
def scopeVariable():
    msg = "updated message is: Hi"
    # Inside method local variable value will be returned
    print(msg)


scopeVariable()
# following msg variable is global variable
print(msg)