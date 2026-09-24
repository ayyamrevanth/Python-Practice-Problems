def unique_once(freq):
    frequency={}
    for i in freq:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    results=[]
    for key in frequency:
        if frequency[key]==1:
            results.append(key)
    return results
freq = [4, 2, 4, 7, 2, 4, 7, 9]
print(unique_once(freq))