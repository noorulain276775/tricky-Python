"""
Tricky List Comprehension Examples for Python Exams

This file contains various challenging list comprehension examples
that test understanding of scope, side effects, and advanced syntax.
"""

print("="*50)
print("TRICKY LIST COMPREHENSION EXAMPLES")
print("="*50)

# Example 1: List comprehension with side effects
print("\n1. List comprehension with side effects:")
x = 1
result = [x for x in range(5)]
print(f"x after list comprehension: {x}")
print(f"result: {result}")

# Example 2: Nested list comprehension
print("\n2. Nested list comprehension:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# Example 3: List comprehension with conditional
print("\n3. List comprehension with conditional:")
numbers = range(10)
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Example 4: List comprehension with multiple conditions
print("\n4. List comprehension with multiple conditions:")
numbers = range(20)
result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {result}")

# Example 5: List comprehension with enumerate
print("\n5. List comprehension with enumerate:")
fruits = ['apple', 'banana', 'cherry']
indexed_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(f"Indexed fruits: {indexed_fruits}")

# Example 6: Complex list comprehension with zip
print("\n6. Complex list comprehension with zip:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']
people = [{'name': name, 'age': age, 'city': city} for name, age, city in zip(names, ages, cities)]
print(f"People: {people}")

# Example 7: List comprehension with function calls
print("\n7. List comprehension with function calls:")
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = [double(x) for x in numbers]
print(f"Doubled: {doubled}")

# Example 8: List comprehension with nested loops
print("\n8. List comprehension with nested loops:")
pairs = [(i, j) for i in range(3) for j in range(2)]
print(f"All pairs: {pairs}")

# Example 9: List comprehension with conditional expression
print("\n9. List comprehension with conditional expression:")
numbers = range(-5, 6)
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"Absolute values: {abs_values}")

# Example 10: List comprehension with string operations
print("\n10. List comprehension with string operations:")
words = ['hello', 'world', 'python', 'programming']
upper_words = [word.upper() for word in words if len(word) > 5]
print(f"Long words in uppercase: {upper_words}")
