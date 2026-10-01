def all_reapting(rept):
    frequency={}
    for i in rept:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    result=[]
    for key in frequency:
        if frequency[key]>1:
            result.append(key)
    return result
rept=[4, 2, 4, 7, 2, 4, 7]
print(all_reapting(rept))