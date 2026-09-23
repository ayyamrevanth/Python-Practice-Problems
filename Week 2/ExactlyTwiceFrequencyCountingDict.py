def twice(freq):
    frequency={}
    for i in freq:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    result=[]
    for key in frequency:
        if frequency[key]==2:
            result.append(key)
    return result
freq=[4, 2, 4, 7, 2, 4, 7]
print(twice(freq))