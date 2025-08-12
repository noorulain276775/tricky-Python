"""
Tricky Generator and Iterator Examples for Python Exams

This file contains various challenging examples involving generators,
iterators, and lazy evaluation concepts.
"""

print("="*50)
print("TRICKY GENERATOR AND ITERATOR EXAMPLES")
print("="*50)

# Example 1: Generator expression vs list comprehension
print("\n1. Generator expression vs list comprehension:")
numbers = [1, 2, 3, 4, 5]
gen = (x**2 for x in numbers)
lst = [x**2 for x in numbers]
print(f"Generator type: {type(gen)}")
print(f"List type: {type(lst)}")

# Example 2: Generator function with yield
print("\n2. Generator function with yield:")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_gen = fibonacci(10)
print(f"Fibonacci generator: {list(fib_gen)}")

# Example 3: Generator with side effects
print("\n3. Generator with side effects:")
def counter():
    count = 0
    while True:
        count += 1
        yield count

c = counter()
print(f"First call: {next(c)}")
print(f"Second call: {next(c)}")
print(f"Third call: {next(c)}")

# Example 4: Generator with send()
print("\n4. Generator with send():")
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Start the generator
print(f"Initial: {acc.send(5)}")
print(f"After 3: {acc.send(3)}")
print(f"After 7: {acc.send(7)}")

# Example 5: Iterator exhaustion
print("\n5. Iterator exhaustion:")
numbers = iter([1, 2, 3, 4, 5])
print(f"First: {next(numbers)}")
print(f"Second: {next(numbers)}")
print(f"Third: {next(numbers)}")
print(f"Fourth: {next(numbers)}")
print(f"Fifth: {next(numbers)}")
try:
    print(f"Sixth: {next(numbers)}")
except StopIteration:
    print("Iterator exhausted!")

# Example 6: Generator with infinite loop
print("\n6. Generator with infinite loop:")
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

inf_counter = infinite_counter()
print(f"First 5 values: {[next(inf_counter) for _ in range(5)]}")

# Example 7: Generator with filter
print("\n7. Generator with filter:")
def even_numbers():
    num = 0
    while True:
        if num % 2 == 0:
            yield num
        num += 1

even_gen = even_numbers()
print(f"First 5 even numbers: {[next(even_gen) for _ in range(5)]}")

# Example 8: Generator with multiple yields
print("\n8. Generator with multiple yields:")
def multi_yield():
    yield "First"
    yield "Second"
    yield "Third"

multi = multi_yield()
print(f"First yield: {next(multi)}")
print(f"Second yield: {next(multi)}")
print(f"Third yield: {next(multi)}")

# Example 9: Generator with return
print("\n9. Generator with return:")
def generator_with_return():
    yield 1
    yield 2
    return "Done"
    yield 3  # This will never execute

gen = generator_with_return()
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")
try:
    print(f"Third: {next(gen)}")
except StopIteration as e:
    print(f"Generator returned: {e.value}")

# Example 10: Generator with close()
print("\n10. Generator with close():")
def generator_with_close():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator closed!")
        return

gen = generator_with_close()
print(f"First: {next(gen)}")
gen.close()

# Example 11: Generator with throw()
print("\n11. Generator with throw():")
def generator_with_throw():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError as e:
        yield f"Caught error: {e}"

gen = generator_with_throw()
print(f"First: {next(gen)}")
print(f"After throw: {gen.throw(ValueError, 'Test error')}")

# Example 12: Generator with context manager
print("\n12. Generator with context manager:")
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")

with timer():
    sum(range(1000000))

# Example 13: Generator with itertools
print("\n13. Generator with itertools:")
import itertools

# Infinite cycle
cycle_gen = itertools.cycle([1, 2, 3])
print(f"Cycle first 7: {[next(cycle_gen) for _ in range(7)]}")

# Count
count_gen = itertools.count(10, 2)
print(f"Count first 5: {[next(count_gen) for _ in range(5)]}")

# Example 14: Generator with tee
print("\n14. Generator with tee:")
original = range(5)
gen1, gen2 = itertools.tee(original)
print(f"First generator: {list(gen1)}")
print(f"Second generator: {list(gen2)}")

# Example 15: Generator with chain
print("\n15. Generator with chain:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = itertools.chain(list1, list2)
print(f"Chained: {list(chained)}")

# Example 16: Generator with islice
print("\n16. Generator with islice:")
infinite = itertools.count()
sliced = itertools.islice(infinite, 10, 20, 2)
print(f"Sliced: {list(sliced)}")

# Example 17: Generator with groupby
print("\n17. Generator with groupby:")
data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
grouped = itertools.groupby(data)
for key, group in grouped:
    print(f"Group {key}: {list(group)}")

# Example 18: Generator with combinations
print("\n18. Generator with combinations:")
letters = ['a', 'b', 'c']
combs = itertools.combinations(letters, 2)
print(f"Combinations: {list(combs)}")

# Example 19: Generator with permutations
print("\n19. Generator with permutations:")
perms = itertools.permutations(letters, 2)
print(f"Permutations: {list(perms)}")

# Example 20: Custom iterator class
print("\n20. Custom iterator class:")
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

countdown = CountDown(5)
print(f"Countdown: {list(countdown)}")
