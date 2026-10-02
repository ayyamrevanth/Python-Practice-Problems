def second_most_frequent(numbers):
    frequency = {}
    # Count frequency
    for i in numbers:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    # Find highest and second-highest frequency
    max_count = 0
    second_count = 0
    most = None
    second = None
    for key in frequency:
        if frequency[key] > max_count:
            second_count = max_count
            second = most
            max_count = frequency[key]
            most = key
        elif frequency[key] > second_count and frequency[key] != max_count:
            second_count = frequency[key]
            second = key
    return second
numbers = [4, 2, 4, 7, 2, 4, 7, 7]
print(second_most_frequent(numbers))