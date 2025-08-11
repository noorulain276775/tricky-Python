import copy

original = [[1, 2], [3, 4]]

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[0].append(99)
original.append([5, 6])

print("Original:      ", original)
print("Shallow Copy:  ", shallow_copy)
print("Deep Copy:     ", deep_copy)
