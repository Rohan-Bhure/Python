import temp
print(__name__)
# It prevents certain code from executing when the file is 
# imported as a module and allows execution only when run directly.

temp.add(4, 4)
def run():
    print("run")
if __name__ == "__main__":
    print("Hello")
    temp.add(4, 5)
    temp.wellcome("reo")
    print(__name__)



# app.py
# def add(a, b):
#     return a + b

# if __name__ == "__main__":  this will run when we excecute this file directly
#     print("Calculator Started")


# 2. __name__
# __name__ is a special built-in variable in Python.
# It tells you the name of the current file/module.

# Example:
# * if file is run directly → __name__ = "__main__"
# * if file is imported → __name__ = module name