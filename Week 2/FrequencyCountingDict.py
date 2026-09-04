def freq_counting(freq):
    frequency={}
    for i in freq:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency
freq=[4, 2, 4, 7, 2, 4, 7]
print(freq_counting(freq))