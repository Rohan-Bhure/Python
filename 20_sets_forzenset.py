# A set is an unordered collection of unique elements.
# Properties:
# No duplicates
# Mutable (can change)
# Unordered
# Fast lookup (O(1) average)
# Uses hashing internally

x = {} # This creates empty dict
x = set() # its a set
x = {2, 5, 6}
x.add(20)
x.remove(6) # error when item is missing
x.discard(100) # no error when item is missing
x.pop() # remove random ele
x.clear()

a ={1,3,5}
b = {5,7,6}
print(a|b) #unique combine
print(a&b) # common ele
print(a^b) #non common ele
print(a-b)
print(20 in x)


# Set elements must be hashable (immutable).
# {1, "hello", (1,2)}
# {[1,2], [3,4]}  Error because lists are mutable and unhashable.




# FrozonSet  -> immutable hasable
fs = frozenset([1, 2, 3])
print(fs)

fs = frozenset([1,2])
d = {fs: "hello"}
print(d)