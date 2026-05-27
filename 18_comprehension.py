# Comprehension is a short and powerful way to create:

# * Lists
# * Dictionaries
# * Sets

# instead of writing long loops.

# It makes code:

# * shorter
# * cleaner
# * faster to write
# * more Pythonic

import math

# 1. Even numbers and their squares from 1 to 20
square_even_num = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers from 1 to 20:", square_even_num)

# 2. Names with length >= 4
names = ["Rohan", "Amit", "Raj", "Priya", "Anjali"]
names_len_more_than_4 = [name for name in names if len(name) >= 4]
print("Names with length >= 4:", names_len_more_than_4)

# 3. Flatten a nested list
arr = [[1, 2], [3, 4], [5, 6]]
flatten_list = [j for row in arr for j in row]
print("Flattened list:", flatten_list)

# 4. Frequency of each character in a word
word = "programming"
freq = {ch: word.count(ch) for ch in set(word)}
print("Character frequency:", freq)

# 5. Dictionary of squares from 1 to 10
dicts = {i: i * i for i in range(1, 11)}
print("Squares dictionary:", dicts)

# 6. Remove vowels from a string
text = "Artificial Intelligence"
vowels = "aeiouAEIOU"
remove_vowels = [ch for ch in text if ch not in vowels]
print("Text without vowels:", remove_vowels)

# 7. Prime numbers from 1 to 100
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

prime_list = [i for i in range(1, 101 if True else 101) if is_prime(i)]
print("Prime numbers from 1 to 100:", prime_list)

# 8. Even numbers -> square, odd numbers -> cube
magic_list = [i * i if i % 2 == 0 else i * i * i for i in range(1, 11)]
print("Magic list:", magic_list)

# 9. Unique letters from a word
word = "machinelearning"
unique_letters = {ch for ch in word}
print("Unique letters:", unique_letters)

# 10. Reverse each word in a list
words = ["python", "django", "react"]
reverse_words = [word[::-1] for word in words]
print("Reversed words:", reverse_words)

# 11. List of tuples using nested comprehension
lis = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print("Tuple list:", lis)

# 12. Filter students with marks > 50
students = {
    "Rohan": 85,
    "Amit": 45,
    "Priya": 92
}

filter_std = {key: value for key, value in students.items() if value > 50}
print("Filtered students:", filter_std)

# 13. Transpose of a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transpose of matrix:", result)

# 14. Common elements in two lists
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

common_elements = [x for x in a if x in b]
print("Common elements:", common_elements)

# 15. Pass/Fail result from student data
data = [
    {"name": "Rohan", "marks": 85},
    {"name": "Amit", "marks": 29},
    {"name": "Priya", "marks": 92}
]

result = {
    item["name"]: "Pass" if item["marks"] >= 50 else "Fail"
    for item in data
}
print("Result:", result)