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
print(is_count(int(input("enter n:"))))