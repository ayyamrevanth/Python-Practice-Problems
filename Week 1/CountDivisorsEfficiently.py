"""num=int(input("enter num:"))
count=0
if num<=0:
    print("enter a positive integer")
else:
    for i in range(1,(int(num**0.5))):
        if i/num:  
            if num/i==i:
                count+=1 
            else:
                count+=2
print(count)"""

#After Gpt Correction
num=int(input("enter num:"))
count=0

if num<=0:
    print("enter a positive int")
else:
    for i in range(1,(int(num**0.5))+1):
        if num%i==0:
            if i*i==num:
                count+=1
            else:
                count+=2
    print(count)