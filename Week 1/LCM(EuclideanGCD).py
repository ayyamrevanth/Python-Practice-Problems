a=int(input("enter a:"))
b=int(input("enter b:"))
x=a
y=b

while y!=0:
    rem=x % y
    x=y
    y=rem
lcm=(a*b)//x                             #Modified / to //. (For LCM, we know the answer is an integer)
print(f"Lcm of {a} and {b} is {lcm}")