# Oops is a Object oriented programing systems.
# used to solved real world problelm by creating classes and objects.
# Real world things makes logical and complex code becomes easy

# class -> is blueprint or template for object or instance.
# object -> is a real world entity which having behavior (methods) + properties(variables)

class Student:
    # class variable -> shared by all objects
    college_id = 1033
    student_count = 0
    __college_lib_id_access = "MBCXON" # private variable only accessed by method
    college_name = "LTRV" 

    # constructor -> called automatically when we create a object
    # parameterized constructor
    def __init__(self, name, batch, roll_no, address):
        self.name = name # instance varibale
        self.batch = batch
        self.roll_no = roll_no
        self.address = address
        self.inc_student_counter()
    
    # instance method
    # getter
    def get_college_lib_access(self):
        return self.__college_lib_id_access
    
    # class method cls is used insted of self
    # for avoiding static variable data change using object 
    @classmethod
    def set_college_name(cls, new_college_name):
        cls.college_name = new_college_name

    @classmethod
    def inc_student_counter(self):
        self.student_count +=1
# object creation

student_1 = Student("Rohan Bhure", 'S', "BE22F05F007", "Neharu Nagar Tumsar")
student_2 = Student("Rohan Bhure", 'S', "BE22F05F007", "Neharu Nagar Tumsar")

print(Student.college_name)
print(student_1.get_college_lib_access()) ## Access of private data

#setting college new name
student_1.set_college_name("GEECS")
print(Student.college_name)

print(Student.student_count)

# self -> current object
# cls -> current class

# static methods not belongs to cls and obj they used inside class only 
# for better orgnization

class Laptop:
    discount = 0.2
    def __init__(self, name):
        self.name = name

    def laptop_price_counter(quantity, price):
        return quantity * price

    @staticmethod # utility / hepler function
    def buy_laptop(quantity, price):
        return quantity * price
    # class my clasName.method_name(x,y) we not use static and instance varibale
    # because static method works independenlty

    def show(self):
        print(self.name) # instance variable access in one method
        print(Student.college_name) # static variable access     

lap1 = Laptop("lenovo")
lap1.buy_laptop(4, 78000)

# instance variable -> properties of individual object
# class variable -> used by all objects
# local variable -> created inside the fuction fun() {x=10;}
# goble variable -> created outside the fuction x =10 fun(){}


# Types of Method
# class method -> created by @classmethod cls is use to access class variable
#                 call by className.method_name()

# instance method -> created method using self parmeter
# static method -> Utility or helper fuctions and not use clss or obj variables
#                   Logic is independent inside the method

