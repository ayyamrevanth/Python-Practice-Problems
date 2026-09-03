def allReapted(lst):
    seen=set()
    repeated=set()
    for i in lst:
        if i in seen:
            repeated.add(i)
        else:
            seen.add(i)
    return repeated
lst=[4,2,5,7,8,2,5]
print(allReapted(lst))