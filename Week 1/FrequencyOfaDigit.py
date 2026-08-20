num=int(input("enter num:"))
a=int(input("enter a:"))
count=0
if (num ==0 and a==0):
    count=1
else:
    while num>0:
        digit=num%10
        if digit==a:
            count+=1
        num=num//10
            
print(f"{a} occurs {count} times")


"""if a < 0 or a > 9:
    print("Invalid digit")""" 

"""What if a = 12?

Your program allows:

Enter a: 12

But 12 isn't a single digit."""