"""
Tricky Unpacking Examples for Python Exams

This file contains various challenging examples involving unpacking,
extended assignment, and sequence operations.
"""

print("="*50)
print("TRICKY UNPACKING EXAMPLES")
print("="*50)

# Example 1: Unpacking with extended assignment
print("\n1. Unpacking with extended assignment:")
a, *b, c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}")

# Example 2: Dictionary unpacking
print("\n2. Dictionary unpacking:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# Example 3: Tuple unpacking in for loop
print("\n3. Tuple unpacking in for loop:")
items = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in items:
    print(f"Number: {num}, Letter: {letter}")

# Example 4: Multiple unpacking
print("\n4. Multiple unpacking:")
first, *middle, last = [1, 2, 3, 4, 5, 6]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Example 5: Unpacking with different lengths
print("\n5. Unpacking with different lengths:")
a, b, *rest = [1, 2]
print(f"a: {a}, b: {b}, rest: {rest}")

# Example 6: Nested unpacking
print("\n6. Nested unpacking:")
data = [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]
for num, (letter1, letter2) in [(1, ('a', 'x')), (2, ('b', 'y'))]:
    print(f"Num: {num}, Letters: {letter1}, {letter2}")

# Example 7: Unpacking in function arguments
print("\n7. Unpacking in function arguments:")
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person = ['Alice', 25, 'NYC']
print_info(*person)

# Example 8: Dictionary unpacking with defaults
print("\n8. Dictionary unpacking with defaults:")
def greet(name, age=30, city='Unknown'):
    print(f"Hello {name}, you are {age} years old from {city}")

person_info = {'name': 'Bob', 'age': 35}
greet(**person_info)

# Example 9: Unpacking with zip
print("\n9. Unpacking with zip:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Example 10: Extended unpacking in assignments
print("\n10. Extended unpacking in assignments:")
*start, end = range(10)
print(f"Start: {start}")
print(f"End: {end}")

# Example 11: Unpacking with enumerate
print("\n11. Unpacking with enumerate:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Example 12: Unpacking nested structures
print("\n12. Unpacking nested structures:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    first, *middle, last = row
    print(f"First: {first}, Middle: {middle}, Last: {last}")

# Example 13: Unpacking with conditional
print("\n13. Unpacking with conditional:")
data = [1, 2, 3, 4, 5]
if len(data) >= 3:
    first, second, *rest = data
    print(f"First: {first}, Second: {second}, Rest: {rest}")

# Example 14: Unpacking in list comprehension
print("\n14. Unpacking in list comprehension:")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
result = [f"{num}: {letter}" for num, letter in pairs]
print(f"Result: {result}")

# Example 15: Complex unpacking patterns
print("\n15. Complex unpacking patterns:")
data = [1, 2, 3, 4, 5, 6, 7, 8]
a, b, *middle, c, d = data
print(f"a: {a}, b: {b}, middle: {middle}, c: {c}, d: {d}")

# Example 16: Unpacking with set
print("\n16. Unpacking with set:")
numbers = {1, 2, 3, 4, 5}
first, *rest = numbers
print(f"First: {first}, Rest: {rest}")

# Example 17: Unpacking in function return
print("\n17. Unpacking in function return:")
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(f"Coordinates: x={x}, y={y}")

# Example 18: Unpacking with range
print("\n18. Unpacking with range:")
start, *middle, end = range(1, 11)
print(f"Start: {start}, Middle: {middle}, End: {end}")

# Example 19: Unpacking with string
print("\n19. Unpacking with string:")
first, *middle, last = "Python"
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Example 20: Unpacking with custom objects
print("\n20. Unpacking with custom objects:")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __iter__(self):
        return iter([self.x, self.y])

point = Point(5, 10)
x, y = point
print(f"Point coordinates: x={x}, y={y}")
