# Strings are collections of charecter
name = "Rohan Bhure"
print(name) # Rohan Bhure
print(name[:]) # Rohan Bhure
print(name[3]) # a
print(name[::-1]) # eruhB nahoR
print(name[2:5]) # han
print(name[::2]) # start, end , step

ls = name.split(" ")
print(len(ls))

ls = ["ravi", "ramesh", "desai"]
full_name = (" ").join(ls)
print(full_name)


print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.strip())
print(name.count("a"))
print(name.replace("o", "O"))
print(name.find("e"))
print(name.startswith("Ro"))
print(name.endswith("Bhure"))
print(name*3) # Rohan Bhure Rohan Bhure Rohan Bhure
print(sorted(name))
print(ord('A'))

# 23) Why Strings Are Immutable
# Benefits:
# * memory optimization
# * hashing support
# * security
# * thread safety

# Because immutable objects can be reused internally.

#List of mutable and unmutable
# mutable -> list , set, dict
# unmutable -> str, tuple, int

print(name.encode())
print(name.decode())