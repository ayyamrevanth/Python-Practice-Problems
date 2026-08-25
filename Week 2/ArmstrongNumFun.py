def is_count(n):
    count=0
    if n==0:
        return 1
    else:
        while n>0:
            dig=n%10
            count+=1
            n//=10
        return count

def armstrong(n):
    count=is_count(n)
    org=n
    armst=0
    while n>0:
        dig=n%10
        armst=armst+(dig**count)
        n//=10
    return armst==org


print(armstrong(int(input("enter num:"))))