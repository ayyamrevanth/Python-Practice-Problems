def sec_small(n):
    small =9
    se_small=9
    if n==0:
        return None                        # print("No second small digit")
    else:
        while n>0:
            digit=n%10
            if small >digit:
                se_small=small                        #Swaping
                small=digit
            elif se_small >digit and digit !=small:    #it will not allow same digits (input like 18233)
                se_small=digit
            n//=10
    #Edge case (input like 11.. or 333..)
    if se_small==9:
        return None
    return se_small
print(sec_small(int(input("enter:"))))