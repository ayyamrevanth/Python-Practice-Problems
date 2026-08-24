def is_Palindrome(n):
    org=n
    rever=0
    while n>0:
        dig=n%10
        rever=rever*10+dig
        n//=10
    if org==rever:
        return True             #insted of if statements we can write (return org == rever) it will give boolean
    else:
        return False
print(is_Palindrome(int(input("enter num:"))))