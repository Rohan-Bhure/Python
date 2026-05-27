# Functions
# * Reusability
# * Clean code
# * Easier debugging
# * Better modular design
# * Easier testing
# * Better teamwork in large projects

# * Parameters are in definition.
# * Arguments are passed during call.
# * return sends result back.
# * print only displays.
# * *args collects extra positional arguments into a tuple.
# * **kwargs collects extra keyword arguments into a dictionary.
# * Lambda is a small anonymous one-line function.
# * Recursion is a function calling itself.
# * Recursion always needs a base case.
# * Python has recursion depth limit.
# * Functions help modularity, testing, and readability.
# function with parameter
def Greet(name : str):
    print(f"Hello, {name}")

def multiplay(num1, num2):
    print(f"{num1} * {num2} = {num1*num2}")

def evenChecker(num):
    if num%2 == 0:
        return true
    else:
        return false


# multiple value return 
def math_ops(a, b):
    return a+b, a-b, a*b
add, sub, mul = math_ops(3, 5)

# *args -> it's a daynamic array . Python provides a set of function to perform 
# oprations on *args . we can pass customize size of array through the function 

# when you do not know how much the parameter size 
def add(*args):
    return sum(args), max(args), min(args)

sums, maxi, min = add(3, 2, 2, 1, 9)
print(f"sums->{sums} maxi->{maxi} min-> {min}")

def kw_fuction(**kwargs):
    print(kwargs) # {'name': 'Rohan', 'age': 22}


def kw_iter(*args, **kwargs):
    for num in args:
        print(num, sep=" ")
    for key, value in kwargs.items():
        print(f"{key} -> {value}", sep=" ")
kw_fuction(name = "Rohan",age = 22)
kw_iter(2, 3, 3, 2, 1, 9, name = "rohan", age =32)



# Lamada function
greet = lambda name : print(f"Hello, {name}")
greet("rohan")

square = lambda num : num**2

print(square(2))

dummy_func = lambda x, y : x**y
print(dummy_func(2, 3))

#nested fuction 
def outer():
    def inner():
        print("inner function")
    return inner
greet = outer()
greet()
