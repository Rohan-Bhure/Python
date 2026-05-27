# A) Base Case
# The stopping condition.

# Without it:

# * recursion never stops
# * stack overflow happens
# * RecursionError occurs
# Every recursive call store in stack and when base case is reached call remove 
# one by one (stackunwinding).

# 1) Factorial using Recursion


# 2) Fibonachi Series



# 3) 

import sys

print(sys.getrecursionlimit())
def fun():
    fun()

data = {
    "name": "Rohan",
    "skills": {
        "backend": ["Python", "FastAPI"],
        "ml": ["TensorFlow", "PyTorch"]
    }
}

def traverse(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(key)
            traverse(value)
    elif isinstance(obj, list): # isinstance used to check obj of which type list, dict
        for item in obj:
            traverse(item)
    else:
        print(obj)

traverse(data)


#1) Sum of digit 
def sum_of_digit(num):
    if(n)