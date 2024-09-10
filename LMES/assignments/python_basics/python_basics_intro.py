# Variables - Types are assigned dynamically
print("printing integer type")
a = 10
print(a)
print(type(a))
#
# print("printing float type")
# b = 10.5
# print(b)
# print(type(b))
#
# print("printing string type")
# c = "Python basics"
# print(c)
# print(type(c))

# Numeric examples

# # Int example
# # Following code print will concatenate two numbers

# print("Enter your integer input a:")
# num1 = input()
# print("Enter your integer input b:")
# num2 = input()
# print("Sum of num1 and num2", (num1 + num2))

# # Following code do sum of two integer using input method
# print("Enter your integer input a:")
# num1 = int(input())
# print("Enter your integer input b:")
# num2 = int(input())
# print("Sum of num1 and num2 = ", (num1 + num2))


# # Float number
# # Following code do sum of two float using input method

# print("Enter your first float number:")
# num1 = float(input("Enter your first float number: "))
# print("Enter your second float number: ")
# num2 = float(input())
# print("Sum of two float numbers = ", (num1 + num2))

# # eval function will accept only integer and float numbers
# print("using eval method to evaluate the number.")
# num1 = eval(input("Enter your first number: "))
# print("Enter your second number: ")
# num2 = eval(input())
# print("Sum of two float numbers = ", (num1 + num2))

# long data type, all integers implementation is long data type in python 3.x
# print("printing long integer type")
# a = 9999*88888
# print(a)
# print(type(a))

# # Operators
# print("Assigning operator and few samples are here:")
# a = 10
# b = 3
#
# print("basic mathematical operators such as +, -, *, /")
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# print("mod: will return reminder 10/3 then it returns 1")
# print(a%b)
# print("String division 10/3 => 3.333 but it returns only integer value and ignore float number so result is 3");
# print(a//b)
# print(a**b)

# Assignment operator
# print("single value assignment:")
# a = 123
# print(a)
#
# # Multiple assignment operator
# print("Multiple value assignment:")
# a,b,c = 10, 20, 30
# print("print a, b, c")
# print(a)
# print(b)
# print(c)

# # Print logical operators
# print("Logical operators examples:")
# a = True
# b = False
# # # AND
# print("Logical AND example")
# print(a and b)
# # # OR
# print("Logical OR example")
# print(a or b)
# # # NOT
# print("Logical NOT example")
# print (not b)

# for loop
# print("for loop iteration using for using range ie, 0 to 7")
# for i in range(8):
#     print("i value is = ", i)
#
# print("for loop iteration using for using range start & end range ie, 11 to 20")
# for i in range(11,21):
#     print("i value is = ", i)
#
# print("for loop iteration to print only even numbers")
# for i in range(21):
#     if i%2 == 0:
#         print(i)

# # printing even numbers
# print("starting range, ending range, step counter, eg: 2, 2+2 = 4, 4+2 = 6")
# for i in range(2,21,2):
#     print(i)
#
# # printing odd numbers
# print("starting range, ending range, step counter, eg: 1, 1+2 = 3, 3+2 = 5")
# for i in range(1,21,2):
#     print(i)

# print("printing reverse order by number 5")
# for i in range(50,20,-5):
#     print(i)


# print("while loop")
# i = 1
# while i<=5:
#     print("Murugaaa")
#     i+=1

# print("while odd numbers")
# i = 2
# while i<=20:
#     print(i)
#     i+=2

# print("while even numbers")
# i = 1
# while i<=20:
#     print(i)
#     i+=2

# print("String")
# print("left to right positive index which starts from 0")
# print("right to left negative index which starts from -1")
# s = "python string"
# print(s)
# print(s[2])
# print(s[-1])

# print("String slicing s[starting index: ending index]")
# print("if start index not provided then by default starts from 0th index")
# print("if ending index not provided then by default slice till last index")
s = "python Course"
# print(s[1:4])
# print(s[0:5])
# print(s[:5])
# print(s[3:])

# print("with step counter ie left to right read")
# # print(s[1:5:2])
# print(s[-5:-1:2])

# print("printing reverse order")
# print(s[::-1])
#
# print("printing length of a string")
# print(len(s))

# print("print string with to lower / upper case method")
# print(s.lower())
# print(s.upper())

# print("swap upper to lower & lower to uppercase to the given string")
# print(s.swapcase())

# print("Every word of first letter to be modified to capitalised ie, title")
# print(s.title())

# print("First letter to be capitalised of a sentence.")
# print(s.capitalize())
#
# s1 = "     Simple String   "
# print(s1)
# print("removing empty spaces on beginning of a string")
# print(s1.strip())

# print("Remove only left side empty string")
# print(s1.lstrip())

# print("Remove only right side empty string")
# print(s1.rstrip())

# print("check isalpha()")
# s2 = "Murugaa123"
# print(s2.isalpha())
# s3 = "Murugaa"
# print(s3.isalpha())

# print("print isdigit()")
# s4 = "Murugaaaa123"
# print(s4.isdigit())
# s5 = "123"
# print(s5.isdigit())
# s7 = "Murugaa@123"
# print(s7.isalnum())
# s6 = "Murugaa123"
# print(s6.isalnum())
# s8 = "Murugaa"
# print(s8.islower())
# s9 = "murugaa"
# print(s9.islower())
# s10 = "Murugaa"
# print(s10.isupper())
# s11 = "MURUGA"
# print(s11.isupper())

# print("List example")
# SimpleList = [10,25,6,78,43,95,25,86,25,70,25]
# print(SimpleList)

# print("Mutable list example")
# SimpleList.append(100)
# print(SimpleList)
#
# print("Indexing are allowed: Find by index")
# print(SimpleList[2])
#
# print("Slicing example")
# print(SimpleList[2:6])
#
# print("Total count of list")
# print("Total number of items in the list: ", len(SimpleList))
#
# print("Find how many times a data present")
# print("25 number is present __ times", SimpleList.count(25))
#
# print("Returning index if given number present in the list")
# print("25 present in the index: ", SimpleList.index(25))
#
# print("Adding a data item to the given index position")
# SimpleList.insert(1, 88)
# print(SimpleList)
#
# print("Removing item from the list but only first occurrence will be deleted")
# SimpleList.remove(25)
# print(SimpleList)
#
# print("Removing item from last index from the list using pop() method")
# SimpleList.pop()
# print(SimpleList)
#
# print("Reversing a list")
# SimpleList.reverse()
# print(SimpleList)
#
# print("Sort by ASC")
# SimpleList.sort()
# print(SimpleList)
#
# print("Sort by DESC")
# SimpleList.sort(reverse=True)
# print(SimpleList)
#
# print("String list")
# StringList = ['f','c','a','x','y','A','X']
# print(StringList)
# StringList.sort()
# print(StringList)
# StringList.sort(reverse=True)
# print(StringList)

# print("Concatenating a List")
# x = [10,20,30]
# y = [40,50,60]
# print(x+y) #[10, 20, 30, 40, 50, 60]
#
# print("Repeating same items given number of times")
# print(x*3) # [10, 20, 30, 10, 20, 30, 10, 20, 30]
#
# print("Finding a value whether present in the list or not")
# print(40 in x) # False
# print(40 not in x) # True

# print("Nested List")
# n = [10,20,[30,40]]
# print(n)
# print(n[0])
# # prints [30,40]
# print(n[2])
# # prints 30
# print(n[2][0])
# # prints 40
# print(n[2][1])

# print("Nest for loop iteration example")
# n = [[10,20,30], [40,50,60], [70,80,90]]
# print(n)
# for item in n:
#     print((item))
#
# for i in range(len(n)):
#     for j in range(len(n[i])):
#         print(n[i][j],end=' ')
#     print()

# print("Tuple Example")
# t = (34,67,81,16,59,73,81,67,81)
# print(t.index(81))
# print(t[1:5])
# print(len(t))
# print(t.count(81))
# print(t.index(59))
# t1 = sorted(t)
# print("sorted tuple & returns as list")
# print(t1)
# print(type(t1))
# print("Least value from the tuple")
# print(min(t))
# print("Max value from the tuple")
# print(max(t))

# print("Parenthesis is optional and it take it as tuple data type")
# t1 = 10,20,30
# t2 = (40,50,60)
# print(t1)
# print(type(t1))
# print(t2)
#
# print("concatenation operator")
# print("concatenation result")
# print(t1+t2)
#
# print("Repeat operator")
# print("print t1 n times")
# print(t1*3)
#
# print("check 10 is there in the tuple or not")
# print(10 in t1)
# print(80 in t1)
#
# numbers1 = (4,1,3,2)
# print(numbers1)
# numbers1 = list(numbers1)
# numbers1.sort(reverse=True)
# numbers2 = tuple(numbers1)
# print("Descending tuple values are")
# print(numbers2)
#
# x1, x2, x3, x4 = numbers2
# print(x1)
# print(x2)

# print("Creating empty tuple")
# emptytuple = ()
# print(emptytuple)
# singlevaluetuple = (10,)
# print("single value tuple")
# print(singlevaluetuple)
# print(type(singlevaluetuple))
# # creating tuple from list
# listfortuple = [10,20,30]
# print("original list")
# print(listfortuple)
# print(type(listfortuple))
# tuplefromlist = tuple(listfortuple)
# print("tuple from list")
# print(tuplefromlist)
# print(type(tuplefromlist))
# # create tuple from range
# tuplerange = tuple(range(10,20,3))
# print(tuplerange)


# print("Set Example")
# s = {10,20,30,40,10,50}
# print('printing set')
# print(s)
# print(type(s))
# # list to set
# listforset = [10,20,30]
# s1 = set(listforset)
# print(s1)
# print(type(s1))

# print("Creating set using range")
# s2 = set(range(10,40,4))
# print(s2)
# print(type(s2))
# empty set creation
# s3 = set()
# print(type(s3))
# s3.add(50)
# print(s3)
# s4 = {10,20,30}
# listone = [40,50,60,]
