"""
Tricky Mutable Object Examples for Python Exams

This file contains various challenging examples involving mutable objects,
default arguments, and unexpected side effects.
"""

print("="*50)
print("TRICKY MUTABLE OBJECT EXAMPLES")
print("="*50)

# Example 1: Mutable default arguments
print("\n1. Mutable default arguments:")
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

# Example 2: List concatenation vs extend
print("\n2. List concatenation vs extend:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"list1 + list2: {list1 + list2}")
print(f"list1 after +: {list1}")
list1.extend(list2)
print(f"list1 after extend: {list1}")

# Example 3: List slicing and assignment
print("\n3. List slicing and assignment:")
a = [1, 2, 3, 4, 5]
a[1:3] = [10, 20, 30]
print(a)

# Example 4: Dictionary with mutable values
print("\n4. Dictionary with mutable values:")
outer_dict = {}
inner_list = [1, 2, 3]
outer_dict['key'] = inner_list
print(f"Original: {outer_dict}")
inner_list.append(4)
print(f"After modifying inner_list: {outer_dict}")

# Example 5: Nested list modification
print("\n5. Nested list modification:")
matrix = [[1, 2], [3, 4]]
copy_matrix = matrix.copy()
matrix[0][0] = 99
print(f"Original matrix: {matrix}")
print(f"Copy matrix: {copy_matrix}")

# Example 6: Set operations with lists
print("\n6. Set operations with lists:")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
intersection = set1 & set2
union = set1 | set2
print(f"Intersection: {intersection}")
print(f"Union: {union}")

# Example 7: Mutable objects in tuples
print("\n7. Mutable objects in tuples:")
t = ([1, 2], [3, 4])
print(f"Original tuple: {t}")
t[0].append(5)
print(f"After modifying: {t}")

# Example 8: List comprehension side effects
print("\n8. List comprehension side effects:")
original = [[1, 2], [3, 4]]
modified = [lst for lst in original]
original[0].append(99)
print(f"Original: {original}")
print(f"Modified: {modified}")

# Example 9: Dictionary comprehension with mutable keys
print("\n9. Dictionary comprehension with mutable keys:")
data = [(1, 'a'), (2, 'b'), (1, 'c')]
result = {k: v for k, v in data}
print(f"Result with duplicate keys: {result}")

# Example 10: Mutable objects in function arguments
print("\n10. Mutable objects in function arguments:")
def modify_list(lst):
    lst.append(999)
    return lst

original = [1, 2, 3]
result = modify_list(original)
print(f"Original: {original}")
print(f"Result: {result}")
print(f"Are they the same object? {original is result}")

# Example 11: List with multiple references
print("\n11. List with multiple references:")
a = [1, 2, 3]
b = a
c = a[:]
a.append(4)
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Example 12: Dictionary with nested structures
print("\n12. Dictionary with nested structures:")
config = {
    'settings': {'theme': 'dark', 'language': 'en'},
    'data': [1, 2, 3, 4]
}
config_copy = config.copy()
config['settings']['theme'] = 'light'
config['data'].append(5)
print(f"Original: {config}")
print(f"Copy: {config_copy}")

# Example 13: Mutable objects in class attributes
print("\n13. Mutable objects in class attributes:")
class Container:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

obj1 = Container()
obj2 = Container()
obj1.add_item('hello')
print(f"obj1 items: {obj1.items}")
print(f"obj2 items: {obj2.items}")

# Example 14: List with generator expression
print("\n14. List with generator expression:")
numbers = [1, 2, 3, 4, 5]
gen = (x**2 for x in numbers)
lst = [x**2 for x in numbers]
print(f"Generator type: {type(gen)}")
print(f"List type: {type(lst)}")

# Example 15: Mutable objects in function return
print("\n15. Mutable objects in function return:")
def create_counter():
    count = [0]
    def increment():
        count[0] += 1
        return count[0]
    return increment

counter1 = create_counter()
counter2 = create_counter()
print(f"Counter1: {counter1()}")
print(f"Counter1: {counter1()}")
print(f"Counter2: {counter2()}")
