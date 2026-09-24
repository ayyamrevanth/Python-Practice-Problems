def count_unique(lst):
    seen=set()
    for i in lst:
        seen.add(i)
    return len(seen)
lst=[4, 2, 4, 7, 2, 4, 7, 9]
print(count_unique(lst))