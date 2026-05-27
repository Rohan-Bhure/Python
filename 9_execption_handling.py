# Execption Handling 
# Execption -> A runtime error that interrupts normal execution of a program.
# It manages error which occures due to code 
# Prevents crashes
# Easy to debug and easy to raise error
# Boast robost backend system
# Handle unexpcted situation

# ZeroDivisionError -> Division by zero
# ValueError -> Invalid value
# TypeError  -> Wrong datatype
# IndexError -> Invalid list index
# KeyError -> Invalid dictionary key
# FileNotFoundError -> File missing
# NameError -> Variable not defined
# AttributeError -> Invalid attribute
# ImportError -> Import failure
# ModuleNotFoundError -> Module missing

#1) Question 1 

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    try:
        c = a/b
    except ZeroDivisionError:
        print("Divid by Zero Error. Can not divid by zero.") 
except TypeError:
    print("Enter valid Type.")
else :
    print(a/b)
    

#Q2 -> Infinite Retry Loop
while True:
    try:
        num = int(input("Enter a valid number : "))
    except ValueError as e :
        print(e)
    else : 
        print("Valid number")
        break

#Q3 -> List Index Safe Access

while True :
    ls = [2,3,3]
    try:
        num = int(input("Enter num : "))
        try:
            print(ls[num])
            break
        except IndexError:
            print("Invalid Index.")
    except ValueError:
        print("Input is not interger")
    else :
        print("Success.")

    
#Q4 -> File Reader with finally
try:
    f = open("ile.txt", "r")
    for line in f:
        print(line)
except FileNotFoundError:
    print("File not available")
else:
    f.close()


#Q5 -> raise a Custome error
class InvalidExceptionError(Exception):
    pass
try:
    age = int(input("Enter a age : "))
    if age < 0 :
        raise print("Age can't be negative")
    if age > 120 :
        raise print("Age not more than 20")
except InvalidExceptionError  :
    print("Age is not vaild")
else :
    print(age)

# Q6 ->  Atm withdrawal


class GreaterAmtThanBalanceError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

balance = 5000

while True:
    try:
        amt = int(input("Enter a withdrawal amount: "))

        if amt < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amt > balance:
            raise GreaterAmtThanBalanceError("Amount is more than balance")

    except ValueError:
        print("Enter a valid number")
    except NegativeAmountError as e:
        print(e)
    except GreaterAmtThanBalanceError as e:
        print(e)
    else:
        balance -= amt
        print("Money withdrawn successfully.")
        print("Current Balance is:", balance)
        break
    finally:
        print("Thank You!")

# Q7 -> without closeing file
try :
    with open("file.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File not found.")

from fastapi import FastAPI, HTTPException
app = FastAPI()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     user = None
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user



class InvalidCredentials(Exception):
    pass


class LoginSystem:
    def login(self, username, password):
        try:
            if username != "admin" or password != "1234":
                raise InvalidCredentials("Invalid username or password")
            print("Login Successful")
        except InvalidCredentials as e:
            print(e)


obj = LoginSystem()

obj.login("admin", "1234")
obj.login("rohan", "abcd")