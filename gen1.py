class MyClass:
    def __str__(self):
        return "str"
    def __repr__(self):
        return "repr"

obj = MyClass()
print(obj)
print([obj])