
def append_element(element, my_list=[]):
    """
    First call: [1] — new list created as default argument initially empty, 1 appended.

    Second call: [1, 2] — same default list used again, now [1, 2].

    Third call: [3] — new list [] explicitly passed, so only 3 in this call.

    Fourth call: [1, 2, 4] — back to default list from before, now appended 4.
    
    """

    my_list.append(element)
    return my_list


print(append_element(1))
print(append_element(2))
print(append_element(3, []))
print(append_element(4))

