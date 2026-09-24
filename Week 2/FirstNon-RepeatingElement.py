def non_repeating(freq):
    frequency={}
    for i in freq:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    for i in freq:
        if frequency[i]==1:
            return i
    if frequency[i]==0:
        return None
freq = [5, 4, 5, 2, 4, 7]
#freq = [4, 2, 4, 2]
print(non_repeating(freq))