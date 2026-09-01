def is_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def is_strong(n):
    org =n
    total=0

    while n>0:
        digit=n%10
        total+=is_fact(digit)
        n//=10
    return org==total
print(is_strong(int(input("enter:"))))