def is_small(n):
    small=9
    if n==0:
        small=0
    else:
        while n>0:
            digit=n%10
            if small>digit:
                small=digit
            n//=10
    return small
print(is_small(int(input("enter :"))))