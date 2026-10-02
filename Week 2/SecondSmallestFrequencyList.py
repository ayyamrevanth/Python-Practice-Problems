def second_small(lst):
    frquency={}
    for i in lst:
        if i in frquency:
            frquency[i]+=1
        else:
            frquency[i]=1
    min_count=9
    sec_min_count=9
    small=None
    sec_small=None
    for key in frquency:
        if frquency[key]<min_count:
            sec_min_count=min_count
            sec_small=small
            min_count=frquency[key]
            small=key
        elif frquency[key]<sec_min_count and frquency[key] !=min_count:
            sec_min_count=frquency[key]
            sec_small=key
    return sec_small
lst = [4, 4, 4, 2, 2, 7, 7, 9]
print(second_small(lst))

