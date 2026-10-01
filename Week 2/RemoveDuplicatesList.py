def remove_dublictes(freq):
    seen=set()
    result=[]
    for i in freq:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
freq = [4, 7, 2, 7, 4, 9, 2]
print(remove_dublictes(freq))