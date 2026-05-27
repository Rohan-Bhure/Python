# # file handling in python is used to perform opretion on files 
# # like writing, reading and specfic updates in file
# # There two ways to open files:
# #1) Using open function  2) Using with open() statement

# f = open("file.txt", "r")
# for line in f:
#     print(line)
# f.close()

# with open("file.txt") as f:
#     for line in f:
#         print(line)
# # no need of closing the file

# with open("file.txt") as f:
#     data = f.read()
#     print(data)

# with open("file.txt") as f:
#     data = f.readlines() # list of lines
#     data1 = f.readable()
#     print(data)
#     print(data1)



# with open("output.txt","w") as f:
#     f.write("hare krishba")


# lines = ["hare krishna\n", "rama mr"]
# with open("output1.txt","w") as f:
#     f.writelines(lines)


# # append data
# with open("log.txt","a") as f:
#     f.write("log is added")


# with open("output.txt", "r") as file:
#     print(file.tell())
#     print(file.read(5))
#     print(file.tell())

# with open("output.txt", "r") as file:
#     file.seek(0)
#     print(file.read())

with open("data.csv", "r") as csv_file:
    data = csv_file.readlines()
    print(data)

import csv

with open("data.csv","r",newline="") as file:
    data = csv.reader(file) # it gives the array like this['name', 'age', 'city']['Rohan', '21', 'Pune']
    for line in data:
        print(line)


# using dictReader

with open("data.csv", "r", newline="") as file :
    data = csv.DictReader(file)
    for line in data:
        print(line) # more use full in real world projects {json object like structure}

# write csv file
data = [
    ["name", "age", "batch"],
    ["Rohan", 20, 'A'],
    ["Mk", 33, 'C']
]
with open("data1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


data = [
    {"name": "Rohan", "age": 21, "city": "Pune"},
    {"name": "Amit", "age": 25, "city": "Mumbai"}
]

with open("datadict.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# json file handling
import json 

with open("data.json","r") as file:
    data = json.load(file)
    print(data)

data ={
    "name": "Rohan",
    "class":"b"
}
with open("data_json.json", "w") as file:
    json.dump(data, file, indent=1)


# String to data 
text = '{"name": "Rohan", "age": 21}'
data = json.loads(text)
print(data)


#json to string
data = {"name": "Rohan", "age": 21}
text = json.dumps(data)
print(text)

#preety json
data = {"name": "Rohan", "age": 21}
print(json.dumps(data, indent=2))

with open("download.jpeg", "rb") as file:
    content = file.read()
    print(content[:20])