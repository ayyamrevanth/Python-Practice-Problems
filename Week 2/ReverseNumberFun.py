def reverse(n):
    rever=0
    while n>0:
        digit=n%10
        rever=rever*10+digit
        n//=10
    return rever
print(reverse(int(input("enter n:"))))