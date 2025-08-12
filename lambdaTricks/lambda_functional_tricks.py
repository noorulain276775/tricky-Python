"""
Tricky Lambda and Functional Programming Examples for Python Exams

This file contains various challenging lambda function examples
that test understanding of closures, late binding, and functional concepts.
"""

print("="*50)
print("TRICKY LAMBDA AND FUNCTIONAL PROGRAMMING EXAMPLES")
print("="*50)

# Example 1: Late binding in closures
print("\n1. Late binding in closures:")
def create_multipliers():
    return [lambda x: i * x for i in range(5)]

multipliers = create_multipliers()
print([m(2) for m in multipliers])

# Example 2: Lambda with map and filter
print("\n2. Lambda with map and filter:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Squared evens: {squared_evens}")

# Example 3: Lambda with reduce
print("\n3. Lambda with reduce:")
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers: {product}")

# Example 4: Lambda with sorted
print("\n4. Lambda with sorted:")
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score: {sorted_by_score}")

# Example 5: Lambda with multiple arguments
print("\n5. Lambda with multiple arguments:")
add = lambda x, y: x + y
multiply = lambda x, y: x * y
print(f"Add: {add(3, 4)}")
print(f"Multiply: {multiply(3, 4)}")

# Example 6: Lambda with conditional expression
print("\n6. Lambda with conditional expression:")
abs_value = lambda x: x if x >= 0 else -x
numbers = [-3, -1, 0, 2, 5]
abs_numbers = [abs_value(x) for x in numbers]
print(f"Absolute values: {abs_numbers}")

# Example 7: Lambda with nested functions
print("\n7. Lambda with nested functions:")
def make_adder(n):
    return lambda x: x + n

add_five = make_adder(5)
add_ten = make_adder(10)
print(f"Add 5 to 3: {add_five(3)}")
print(f"Add 10 to 7: {add_ten(7)}")

# Example 8: Lambda with list comprehension
print("\n8. Lambda with list comprehension:")
functions = [lambda x, i=i: x + i for i in range(5)]
results = [f(10) for f in functions]
print(f"Results: {results}")

# Example 9: Lambda with filter and map chaining
print("\n9. Lambda with filter and map chaining:")
numbers = range(1, 21)
result = list(map(lambda x: x**2, filter(lambda x: x % 3 == 0, numbers)))
print(f"Square of numbers divisible by 3: {result}")

# Example 10: Lambda with complex logic
print("\n10. Lambda with complex logic:")
process = lambda x: (x**2 + 1) if x % 2 == 0 else (x**3 - 1)
numbers = [1, 2, 3, 4, 5]
processed = [process(x) for x in numbers]
print(f"Processed numbers: {processed}")

# Example 11: Lambda with string operations
print("\n11. Lambda with string operations:")
words = ['hello', 'world', 'python', 'programming']
length_check = lambda word: len(word) > 5
long_words = list(filter(length_check, words))
print(f"Long words: {long_words}")

# Example 12: Lambda with dictionary operations
print("\n12. Lambda with dictionary operations:")
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = dict(filter(lambda item: item[1] % 2 == 0, data.items()))
print(f"Even values: {filtered}")

# Example 13: Lambda with tuple unpacking
print("\n13. Lambda with tuple unpacking:")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
swapped = list(map(lambda pair: (pair[1], pair[0]), pairs))
print(f"Swapped pairs: {swapped}")

# Example 14: Lambda with nested lambda
print("\n14. Lambda with nested lambda:")
outer = lambda x: lambda y: x + y
add_three = outer(3)
result = add_three(7)
print(f"Result of nested lambda: {result}")

# Example 15: Lambda with default arguments
print("\n15. Lambda with default arguments:")
default_adder = lambda x, y=10: x + y
print(f"Default add: {default_adder(5)}")
print(f"Custom add: {default_adder(5, 20)}")
