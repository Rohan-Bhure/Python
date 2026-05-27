print("Hare krishna")

# variables are the names for storing the data .
# data are of many types :
# 1) Numeric data -> int, float, double
#.   num = 5, float_num  = 0.5f, double_num = 0.555
#.   4 bytes, 4 bytes, 8 bytes
# 2) String and char
#    name = "Rohan" char = 'c' // 1 bytes
# 3) Boolean flag = true/false
#  

# List 
ls = [1, 3, "rohan"] 
for i in ls:
    print(ls)
# list is mutable dynnamic ds

# Tuple
tuple = (2, 3, 4)
for i in tuple:
    print(i)
# tuple are immutable we can't change after 

#Dict (key-value pair)

person = {
    "name" : "Rohan",
    "age" : 20,
    "class" :3,
}

for key, value in person.items() :
    print(f"{key} -> {value}")

# Set (stores unique values)
sets = {1, 3, 6, 6, "rohan"}
for i in sets:
    print(i)

# type checking
print(type(sets))


# Type Convesrion
num = int("123")
age = str(21)

# Input

num = int(input("Enter a number"))

#Arithmatic Operaters
# *, /, +, -, %

# Logical Operaters
# and or not

# Comparison 
# >, <, ==, !=, >=, <=

# Assignment Operaters
# a+=10 , a-=10, 

# Indentation Error
# if True:
# print("Hello"). // code should arranged properly otherwise gives error


# Mutable and Immutable 
# Object cannot be changed after creation
# If you modify it, Python creates a NEW object.
# | Data Type   | Immutable? |
# | ----------- | ---------- |
# | `int`       | Yes        |
# | `float`     | Yes        |
# | `complex`   | Yes        |
# | `bool`      | Yes        |
# | `str`       | Yes        |
# | `tuple`     | Yes        |
# | `frozenset` | Yes        |
# | `bytes`     | Yes        |
# | `range`     | Yes        |

# Object can be modified after creation
# Same memory location changes.

# | Data Type   | Mutable? |
# | ----------- | -------- |
# | `list`      | Yes      |
# | `dict`      | Yes      |
# | `set`       | Yes      |
# | `bytearray` | Yes      |

a = "python"
b = "python"

print(a is b) # True because both point to same object.
print(a)
print(b)


for _ in range(6):
    print(_)