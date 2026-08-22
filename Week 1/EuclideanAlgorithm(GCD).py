a=int(input("enter a:"))
b=int(input("enter b:"))
"""if b==0:
    a=0             # for GCD(10, 0) = 10,so no need if b==0.
else:"""

while b !=0:   #changed after the correction(min(a,b)>0)
    reminder=a%b
    a=b
    b=reminder
print(a)