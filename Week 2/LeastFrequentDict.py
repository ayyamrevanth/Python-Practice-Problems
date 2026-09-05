def least_frequency(freq):
    frequnency={}
    for i in freq:
        if i in frequnency:
            frequnency[i]+=1
        else:
            frequnency[i]=1
    min_count=9
    least_frequent=None
    for key in frequnency:
        if min_count>frequnency[key]:
            min_count=frequnency[key]
            least_frequent=key
    return least_frequent
freq = [4, 2, 4, 7, 2, 4, 7, 9]
print(least_frequency(freq))