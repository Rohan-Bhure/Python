# Collections -> are the data Structure which use to manage 
# data in specific way 
# List -> It's mutable, ordered, allow duplicate dynamic in size, and we can store any type of data
# Set -> immutable stores unique values
# Dict -> Store data in key-value pair . Used wiedly in internet to share data in json formate
# Tuple -> store immutable data 

ls = [1, 3, 4, 3]
tuples = (1, 3, 5, "Epple")
dict = {}
sets = {3,3,55,44,44} #unique element store


# Important list methods
ls.append(3)
ls[1] = 44 # mutable
print(ls)
ls.remove(1)
print(ls)
print(ls.reverse())
ls.sort()
print(ls) 
ls.extend([1, 3, 4])
print(ls)



# pop()
student = {
    "course" : "en",
    "name" : "e"
}
removed = student.pop("course")
last_item = student.popitem() # last inserted deteleted

student.update({
    "city": "Pune",
    "skills": ["Python", "Django"]
})



print(student.keys())
print(student.values())
print(student.items())

print("name" in student)
print("salary" in student)


# sorted_marks = dict(sorted(marks.items()))

# del dict


nums =(3, 5, 1)
print("13. Repetition")
print((1, 2) * 3)
print()
print(nums.index(3))
sorted_tuple = tuple(sorted(nums))

colors = ("red", "green", "blue")
for index, value in enumerate(colors):
    print(index, value)

names = ("Rohan", "Amit", "Priya")
marks = (90, 80, 95)
zipped = tuple(zip(names, marks))
print("22. zip()")
print(zipped)
print()