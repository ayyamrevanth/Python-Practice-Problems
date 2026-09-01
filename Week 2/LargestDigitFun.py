def largest_digit(n):
    larg=0
    while n>0:
        digit=n%10
        if larg<digit:
            larg=digit
        n//=10
    return larg
print(largest_digit(int(input("enter :"))))