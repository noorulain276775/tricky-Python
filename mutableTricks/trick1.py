def append_to_list(value, my_list=[]):
    """
    Appends 'value' to 'my_list'. Demonstrates the mutable default argument trap.

    Args:
        value: The value to append.
        my_list (list, optional): List to append to. Defaults to an empty list.

    Returns:
        list: The updated list.

    Behavior:
        Because the default list is created once at function definition, 
        calling this function multiple times without specifying 'my_list' 
        will keep adding to the same list.

    Example:
    >>> append_to_list(1)
    [1]
    >>> append_to_list(2)
    [1, 2]
    >>> append_to_list(3)
    [1, 2, 3]
    """
    my_list.append(value)
    return my_list


print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))
