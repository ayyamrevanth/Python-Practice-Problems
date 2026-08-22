num=int(input("enter num:"))
original=num
a=num
count =0
total=0

while num>0:
    num=num//10
    count+=1
while original>0:
    digit=original%10
#    if digit>0:                          No need of if,this (digit=original%10) will give int grom 0-9
    total=total+(digit**count)
    original=original//10
if total==a:
    print(f"{a} is an Armstrong Number ")
else:
    print(f"{a} Not an Armstrong Number")