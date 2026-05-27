# An iterator is an object that gives values one by one.
# A generator is a simple way to create iterators.
# All generators are iterators, but not all iterators are generators.
# An object you can loop over is iterator
# list ,tuple ,string ,set ,dict 
nums = [1, 2, 3, 4]
for x in nums: # nums is iterable
    print(x) 

# Iterator
# An object that remembers its current position and gives the next value each time.
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
# After values are finished, next(it) raises StopIteration.

# An object is an iterator if it has:
# __iter__() returns the iterator object itself
# __next__() returns the next item

nums = {"name": "Rohan",
        "age": 20}

print(hasattr(nums, "__iter__")) # True
print(hasattr(nums, "__next__")) # False

it = iter(nums)
print(hasattr(it, "__next__")) # True


# genrator creates automatically __iter__ and __next__
nums = [x for x in range(1000000)] #  Stror everything in mermory
gen = (x for x in range(1000000)) # Genrate one value at time


nums = (x*x for x in range(2)) 
print(next(nums))
print(next(nums))
print(next(nums,"End"))

def gens():
    yield 1 # puses the function execution saves the state 
    yield 2
    yield 3

fun = gens()
print(next(fun))
print(next(fun))
print(next(fun))
print(next(fun,"End"))


class ReverseList1:
    def __init__(self,ls):
        self.ls = ls
        self.length = len(ls) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.length < 0:
            raise StopIteration
        
        value = ls[self.length]
        self.length -= 1
        return value
            

ls = [2, 4 ,5 ,6 ,9]
lst = ReverseList1([2, 4 ,5 ,6 ,9])
for i in lst:
    print(i)


def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)


class Counter:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x > 5:
            raise StopIteration
        value = self.x
        self.x += 1
        return value


obj = Counter()

print(next(obj))
print(next(obj))




def count():
    for i in range(1, 6):
        yield i

count()
count()

# Because generators automatically implement:__iter__(), __next__()
# Every generator is an iterator

