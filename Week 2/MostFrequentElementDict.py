def most_freq(freq):
    frequency={}
    for i in freq:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    max_count=0
    most_frequent=None
    for key in frequency:
        if frequency[key]>max_count:
            max_count=frequency[key]
            most_frequent=key
    return most_frequent
freq=[4, 2, 4, 7, 2, 4, 7]
print(most_freq(freq))