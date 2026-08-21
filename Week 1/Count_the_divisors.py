num=int(input("enter num:"))
count=0

if num<=0:
    print("Enter a positive integer to divide")
else:
    for i in range(1,num+1):
        if num%i==0:
            count+=1
            
    print(count)