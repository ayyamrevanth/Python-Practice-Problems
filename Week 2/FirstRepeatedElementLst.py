def first_element(numbers):

    seen = set()

    for i in numbers:
        if i in seen:
            return i
        else:
            seen.add(i)
    return i

numbers = [4, 7, 2, 7]
print(first_element(numbers))