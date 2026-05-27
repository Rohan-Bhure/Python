# Control Flow

num = int(input("Enter a num : "))
if (num%2) == 0:
    print("Even no")
else:
    print("Odd no")


gender = chr(input("Enter your gender : M, F, O(Other)"))
age = int(input("Enter your age : "))
if gender is 'M':
    print("Yor are Male.")
    if age >= 18 :
        print("You can use this application")
    else :
        print("You can't use this application. Minimum age 18 is allowed")
elif gender is 'F':
    print("Yor are Female.")
    if age >= 18 :
        print("You can use this application")
    else :
        print("You can't use this application. Minimum age 18 is allowed")
else :
    print("You are other , NO ENTERY")



# Match - case
status_code = 404

match status_code:
    case 200:
        print("Success")

    case 401:
        print("Unauthorized")

    case 404:
        print("Not Found")

    case 500:
        print("Server Error")

    case _:
        print("Unknown Error")






# is is used to compare memory location , == equals checks the values
# in checks the value in object // Return True, False
# R in name

if "Python" in "Python is Simple lang" :
    print("Python word is found")
# not in also 