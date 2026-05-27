# Loops
import sys
for i in range(1, 10):
    print(i)

student = {
    "name" : "Rohan",
    "age" : 20,
    "batch" : "A"
}

for value in student.values():
    print(f"{value} ->")

for key in student.keys():
    print(key)

for key, value in student.items() :
    print(f"{key} -> {value}")

x = int(input("Enter a value of x > 10 : "))
while x > 10:
    print(x)
    x-=1

# do-while is not used in python

for i in range(1, 10, 2):
    print(i)


# Complex Example

company = {
    "name": "TechNova",
    "departments": {
        "AI": {
            "manager": "Rohan",
            "employees": [
                {
                    "id": 101,
                    "name": "Amit",
                    "salary": 75000,
                    "skills": ["Python", "ML", "TensorFlow"]
                },
                {
                    "id": 102,
                    "name": "Sneha",
                    "salary": 82000,
                    "skills": ["Python", "NLP"]
                }
            ]
        },

        "Backend": {
            "manager": "Priya",
            "employees": [
                {
                    "id": 201,
                    "name": "Rahul",
                    "salary": 68000,
                    "skills": ["NodeJS", "MongoDB"]
                },
                {
                    "id": 202,
                    "name": "Kiran",
                    "salary": 72000,
                    "skills": ["FastAPI", "PostgreSQL", "Docker"]
                }
            ]
        }
    },

    "projects": [
        {
            "project_name": "Pothole Detection",
            "team": ["Amit", "Rahul"],
            "budget": 500000
        },
        {
            "project_name": "Credit Risk AI",
            "team": ["Sneha", "Kiran"],
            "budget": 800000
        }
    ]
}


# 1. Print all department names.
# 2. Print names of all employees.
# 3. Find employees whose salary is greater than 70000.
# 4. Find all employees who know "Python".
# 5. Find the employee with the highest salary.

for  dept in company["departments"].values():
     for emps in dept["employees"]:
        if emps["salary"] > 70000 :
            print(f'{emps["name"]} -> {str(emps["salary"])}')
     
for dept in company["departments"]:
    print(dept)
    
for dept in company["departments"].values():
        for emps in dept["employees"]:
             print(emps["name"])


# for dept in company["departments"]:
#     print(dept)


for dept in company["departments"].values():
    for emp in dept['employees']:
        for skills in emp["skills"]:
            if "Python" in skills:
                print(f"{emp['name']} -> Python")

salray_max = 0
name = ""
for dept in company["departments"].values():
    for emp in dept["employees"]:
        if emp['salary'] > salray_max :
            salray_max = emp['salary']
            name = emp['name']
print(f"{salray_max} -> {name}")


# check properly every traversing of obj and list 
# items() , values(), keys() when we use also check properly